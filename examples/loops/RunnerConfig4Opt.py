from datetime import datetime
from EventManager.Models.RunnerEvents import RunnerEvents
from EventManager.EventSubscriptionController import EventSubscriptionController
from ConfigValidator.Config.Models.RunTableModel import RunTableModel
from ConfigValidator.Config.Models.FactorModel import FactorModel
from ConfigValidator.Config.Models.RunnerContext import RunnerContext
from ConfigValidator.Config.Models.OperationType import OperationType
from ExtendedTyping.Typing import SupportsStr
from ProgressManager.Output.OutputProcedure import OutputProcedure as output

from typing import Dict, List, Any, Optional
from pathlib import Path
from os.path import dirname, realpath
import subprocess
import signal
import time
import shlex
import os
import random
import pandas as pd

class RunnerConfig:
    ROOT_DIR = Path(dirname(realpath(__file__)))
    timestamp_start = None
    timestamp_end = None

    # ================================ USER SPECIFIC CONFIG ================================
    name: str = "loop_experiment"
    results_output_path: Path = ROOT_DIR / 'experiments_loops2_58opt'
    operation_type: OperationType = OperationType.AUTO
    time_between_runs_in_ms: int = 3000
    num_runs = 6 

    loop_execution_counts = {
        'loop5': 0,
        'loop6': 0,
        'loop7': 0,
        'loop8': 0
    }

    def __init__(self):
        """Executes immediately after program start, on config load"""
        EventSubscriptionController.subscribe_to_multiple_events([
            (RunnerEvents.BEFORE_EXPERIMENT, self.before_experiment),
            (RunnerEvents.BEFORE_RUN, self.before_run),
            (RunnerEvents.START_RUN, self.start_run),
            (RunnerEvents.START_MEASUREMENT, self.start_measurement),
            (RunnerEvents.INTERACT, self.interact),
            (RunnerEvents.STOP_MEASUREMENT, self.stop_measurement),
            (RunnerEvents.STOP_RUN, self.stop_run),
            (RunnerEvents.POPULATE_RUN_DATA, self.populate_run_data),
            (RunnerEvents.AFTER_EXPERIMENT, self.after_experiment)
        ])
        self.run_table_model = None

        output.console_log("Custom config loaded")

    def create_run_table_model(self) -> RunTableModel:
        """Create and return the run_table model here."""
        factor1 = FactorModel("run_number", [f'r{i}' for i in range(1, self.num_runs + 1)])
        factor4 = FactorModel("optimization", ['yes'])
        factor5 = FactorModel("loop_type",['loop5_opt_cacheblocking', 'loop5_opt_unrolling', 'loop6_opt_cacheblocking', 'loop6_opt_collapsing', 'loop6_opt_predicate', 'loop6_opt_unrolling', 'loop7_opt_cacheblocking', 'loop7_opt_predicate', 'loop7_opt_unrolling', 'loop8_opt_predicate'])
        self.run_table_model = RunTableModel(
            factors=[factor1, factor4, factor5],
            data_columns=['execution_time', 'cpu_usage', 'memory_usage', 'energy_usage'],
            shuffle=True
        )
        return self.run_table_model

    def before_experiment(self) -> None:
        """Perform any activity required before starting the experiment here."""
        output.console_log("Config.before_experiment() called!")

    def before_run(self) -> None:
        """Perform any activity required before starting a run."""
        self.timestamp_start = datetime.now()

    def start_run(self, context: RunnerContext) -> None:
        """Perform any activity required for starting the run here."""
        loop_type = context.run_variation['loop_type']
        optimization = context.run_variation['optimization']

        file_name = loop_type + '.py'
        self.target = subprocess.Popen(['python3', f'examples/loops/loops2/{file_name}'])
        output.console_log(f"Started run for {loop_type}.")

    def start_measurement(self, context: RunnerContext) -> None:
        """Perform any activity required for starting measurements."""
        
        csv_file_path = context.run_dir / "powerjoular.csv"

        powerjoular_cmd = f'powerjoular -tp {self.target.pid} -f {csv_file_path}'
        time.sleep(1)

        self.energy_profiler = subprocess.Popen(shlex.split(powerjoular_cmd))

        performance_profiler_cmd = f"ps -p {self.target.pid} --noheader -o %cpu,%mem"
        print('%cpu,%mem')
        timer_cmd = f"while true; do {performance_profiler_cmd}; sleep 1; done"
        self.performance_profiler = subprocess.Popen(['sh', '-c', timer_cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output.console_log("Started measurement for CPU and memory usage and energy usage.")

    def interact(self, context: RunnerContext) -> None:
        """Perform any interaction with the running target system here."""
        output.console_log("Waiting for the loop to complete...")
        self.target.wait()

    def stop_measurement(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping measurements."""
        os.kill(self.energy_profiler.pid, signal.SIGINT)
        self.energy_profiler.wait()
        self.performance_profiler.kill()
        self.performance_profiler.wait()
        output.console_log("Stopped cpu and memory measurement.")

    def stop_run(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping the run."""
        self.target.kill()
        self.target.wait()
        self.timestamp_end = datetime.now()
        output.console_log("Config.stop_run() called!")

    def populate_run_data(self, context: RunnerContext) -> Optional[Dict[str, Any]]:
        """Parse and process any measurement data here."""
        psdf = pd.DataFrame(columns=['cpu_usage', 'memory_usage'])
        for i, l in enumerate(self.performance_profiler.stdout.readlines()):
            decoded_line = l.decode('ascii').strip()
            decoded_arr = decoded_line.split()
            if len(decoded_arr) < 2:
                print(f"Skipping invalid line: {decoded_line}")
                continue
            cpu_usage = float(decoded_arr[0])
            memory_usage = float(decoded_arr[1])
            psdf.loc[i] = [cpu_usage, memory_usage]
            
        psdf.to_csv(context.run_dir / 'raw_data.csv', index=False)
        print("CPU percentage,memory values", decoded_arr)

        output_file = f'{context.run_dir}/powerjoular-filtered-data.csv-{self.target.pid}.csv'
        df = pd.read_csv(context.run_dir / f"powerjoular.csv-{self.target.pid}.csv")

        df['CPU Utilization'] = pd.to_numeric(df['CPU Utilization'], errors='coerce')
        df['CPU Power'] = pd.to_numeric(df['CPU Power'], errors='coerce')

        filtered_df = df.dropna(subset=['CPU Utilization', 'CPU Power'])

        for column in filtered_df.columns[1:]:
            filtered_df[column] = filtered_df[column].astype(float)

        filtered_df.to_csv(output_file, index=False)
        
        run_data = {
            'execution_time': (self.timestamp_end - self.timestamp_start).total_seconds(),
            'cpu_usage': round(psdf['cpu_usage'].mean(), 3),
            'memory_usage': round(psdf['memory_usage'].mean(), 3),
            'energy_usage': round(filtered_df['CPU Power'].sum(), 3)
        }
        return run_data

    def after_experiment(self) -> None:
        """Perform any activity required after stopping the experiment here."""
        output.console_log("Config.after_experiment() called!")
        
    experiment_path: Path = None
