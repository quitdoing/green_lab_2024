library(dplyr)

# Read the CSV files containing the data for original loops (loop1 to loop10)
df_original_loops <- read.csv("run_table-1.csv")  # Contains loop1, loop2, ..., loop10

# Read the CSV file containing data for all optimized loops (for each original loop)
df_optimized_loops <- read.csv("run_table-2.csv")  # Contains optimized loops for each loop1, loop2, ...

# Number of loops you have (e.g., loop1 to loop10)
num_loops <- 10

# Assign 'looptype' to the original loops (loop1 to loop10)
# Assuming each original loop corresponds to one row per loop
df_original_loops <- df_original_loops %>%
  mutate(looptype = rep(paste("loop", 1:num_loops, sep=""), each = nrow(df_original_loops) / num_loops))

# Assign 'looptype' for each optimized loop (for loop1, loop2, ..., loop10)
# Assuming each loop has 3 optimizations (e.g., cacheblocking, unrolling, batching)
df_optimized_loops <- df_optimized_loops %>%
  mutate(looptype = rep(c(
    "loop1_opt_cacheblocking", "loop1_opt_unrolling", "loop1_opt_batching", 
    "loop2_opt_cacheblocking", "loop2_opt_unrolling", "loop2_opt_batching", 
    "loop3_opt_cacheblocking", "loop3_opt_unrolling", "loop3_opt_batching",
    "loop4_opt_cacheblocking", "loop4_opt_unrolling", "loop4_opt_batching",
    "loop5_opt_cacheblocking", "loop5_opt_unrolling", "loop5_opt_batching",
    "loop6_opt_cacheblocking", "loop6_opt_unrolling", "loop6_opt_batching",
    "loop7_opt_cacheblocking", "loop7_opt_unrolling", "loop7_opt_batching",
    "loop8_opt_cacheblocking", "loop8_opt_unrolling", "loop8_opt_batching",
    "loop9_opt_cacheblocking", "loop9_opt_unrolling", "loop9_opt_batching",
    "loop10_opt_cacheblocking", "loop10_opt_unrolling", "loop10_opt_batching"
  ), each = nrow(df_optimized_loops) / (num_loops * 3)))  # Adjust 'each' based on the number of rows per optimization

# Combine the original loops and the optimized loops data into one data frame
df_all <- bind_rows(df_original_loops, df_optimized_loops)

# Calculate descriptive statistics (mean, median, sd) for each loop type
summary_stats <- df_all %>%
  group_by(looptype) %>%  # Group data by looptype (e.g., loop1, loop1_opt_cacheblocking, etc.)
  summarise(
    # Calculate descriptive statistics (mean, median, sd) for each loop type
        # Execution Time Statistics
        mean_execution_time = round(mean(execution_time, na.rm = TRUE), 2),
        median_execution_time = round(median(execution_time, na.rm = TRUE), 2),
        sd_execution_time = round(sd(execution_time, na.rm = TRUE), 2),
        
        # CPU Usage Statistics
        mean_cpu_usage = round(mean(cpu_usage, na.rm = TRUE), 2),
        median_cpu_usage = round(median(cpu_usage, na.rm = TRUE), 2),
        sd_cpu_usage = round(sd(cpu_usage, na.rm = TRUE), 2),
        
        # Memory Usage Statistics
        mean_memory_usage = round(mean(memory_usage, na.rm = TRUE), 2),
        median_memory_usage = round(median(memory_usage, na.rm = TRUE), 2),
        sd_memory_usage = round(sd(memory_usage, na.rm = TRUE), 2),
        
        # Energy Usage Statistics
        mean_energy_usage = round(mean(energy_usage, na.rm = TRUE), 2),
        median_energy_usage = round(median(energy_usage, na.rm = TRUE), 2),
        sd_energy_usage = round(sd(energy_usage, na.rm = TRUE), 2)

  )

# View the calculated summary statistics
write.csv(summary_stats, "comparison_all_loops1.csv", row.names = FALSE)






