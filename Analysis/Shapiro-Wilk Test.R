library(dplyr)

# Function to handle Shapiro-Wilk test and avoid errors for constant data
safe_shapiro_test <- function(data) {
  if (length(unique(data)) == 1) {
    return(list(statistic = NA, p.value = NA))  # Return NA if all values are identical
  } else {
    return(shapiro.test(data))  # Perform Shapiro-Wilk test if data is not constant
  }
}

# Read and combine the original and optimized data
df_original <- read.csv("run_table-1.csv")  # Data for loop1 to loop10
df_optimized <- read.csv("run_table-2.csv")  # Data for optimized loops

df_all <- bind_rows(df_original, df_optimized)

# Filter the data to include only the relevant columns for each metric
df_energy_usage <- df_all %>%
  select(loop_type, energy_usage)

df_execution_time <- df_all %>%
  select(loop_type, execution_time)

df_cpu_usage <- df_all %>%
  select(loop_type, cpu_usage)

df_memory_usage <- df_all %>%
  select(loop_type, memory_usage)

# Perform the Shapiro-Wilk test for each metric (energy usage, execution time, etc.)

# Energy Usage
shapiro_results_energy_usage <- df_energy_usage %>%
  group_by(loop_type) %>%  # Group by loop_type
  summarise(
    shapiro_test = list(safe_shapiro_test(energy_usage)),  # Use safe_shapiro_test to handle constant data
    .groups = 'drop'
  ) %>%
  mutate(
    W_statistic = sapply(shapiro_test, function(x) x$statistic),
    p_value = sapply(shapiro_test, function(x) x$p.value)
  ) %>%
  select(loop_type, W_statistic, p_value)

# Execution Time
shapiro_results_execution_time <- df_execution_time %>%
  group_by(loop_type) %>%
  summarise(
    shapiro_test = list(safe_shapiro_test(execution_time)),
    .groups = 'drop'
  ) %>%
  mutate(
    W_statistic = sapply(shapiro_test, function(x) x$statistic),
    p_value = sapply(shapiro_test, function(x) x$p.value)
  ) %>%
  select(loop_type, W_statistic, p_value)

# CPU Usage
shapiro_results_cpu_usage <- df_cpu_usage %>%
  group_by(loop_type) %>%
  summarise(
    shapiro_test = list(safe_shapiro_test(cpu_usage)),
    .groups = 'drop'
  ) %>%
  mutate(
    W_statistic = sapply(shapiro_test, function(x) x$statistic),
    p_value = sapply(shapiro_test, function(x) x$p.value)
  ) %>%
  select(loop_type, W_statistic, p_value)

# Memory Usage
shapiro_results_memory_usage <- df_memory_usage %>%
  group_by(loop_type) %>%
  summarise(
    shapiro_test = list(safe_shapiro_test(memory_usage)),
    .groups = 'drop'
  ) %>%
  mutate(
    W_statistic = sapply(shapiro_test, function(x) x$statistic),
    p_value = sapply(shapiro_test, function(x) x$p.value)
  ) %>%
  select(loop_type, W_statistic, p_value)

# Save the results to CSV files
write.csv(shapiro_results_energy_usage, "shapiro_wilk_test_results_energy_usage.csv", row.names = FALSE)
write.csv(shapiro_results_execution_time, "shapiro_wilk_test_results_execution_time.csv", row.names = FALSE)
write.csv(shapiro_results_cpu_usage, "shapiro_wilk_test_results_cpu_usage.csv", row.names = FALSE)
write.csv(shapiro_results_memory_usage, "shapiro_wilk_test_results_memory_usage.csv", row.names = FALSE)

# Perform Kruskal-Wallis test for execution_time across loop_type
#kruskal_results <- kruskal.test(execution_time ~ loop_type, data = df_all)

# Print the test results
#print(kruskal_results)

