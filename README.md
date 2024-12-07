# Green_Lab_2024_ROOT!

Course project repository for Green Lab 2024

# __`master` branch__

For Experiment-Runner part and loops, as well as Running Configurations it is possible to switch to the __`master`__ branch.

## Run Tables

- Run table for non-optimized loops is in `examples/loops/experiments_loops_no/loop_experiments_resit`.
- Run table for optimized loops is in `examples/loops/experiments_loops_yes/loop_experiments_resit`.

## Replicating Experiments

To replicate experiments, set up Experiment Runner and EnergiBridge, then run:

```bash
python experiment-runner/ examples/loops/RunnerConfigNo.py
```

for non-optimized loops, and:

```bash
python experiment-runner/ examples/loops/RunnerConfigOpt.py
```

for optimized loops.

## Data Analysis

The data analysis part is located in the `Analysis` folder.

To run a specific test, execute the corresponding `.R` file with the name of the test.
