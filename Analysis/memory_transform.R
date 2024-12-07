library(dplyr)

# Load the datasets
df1 <- read.csv("run_table-1.csv")
df2 <- read.csv("run_table-2.csv")

# Combine the two datasets into one
df <- bind_rows(df1, df2)

# Perform log transformation
df <- df %>%
  mutate(
    log_memory_usage = log(memory_usage)  # Log-transform memory usage
  )

# Perform the Shapiro-Wilk normality test for log-transformed data
log_shapiro_results <- df %>%
  group_by(loop_type) %>%
  filter(n_distinct(log_memory_usage) > 1) %>%  # Only include groups with more than one unique value
  summarise(
    sw_test = list(shapiro.test(log_memory_usage)),  # Conduct Shapiro-Wilk test
    .groups = 'drop'
  )

# Extract W-statistic and p-value for log-transformed data
log_shapiro_results <- log_shapiro_results %>%
  mutate(
    W_statistic = sapply(sw_test, function(x) x$statistic),
    p_value = sapply(sw_test, function(x) x$p.value)
  ) %>%
  select(loop_type, W_statistic, p_value)

# Handle groups with constant values
constant_log_groups <- df %>%
  group_by(loop_type) %>%
  summarise(
    constant = n_distinct(log_memory_usage) == 1,
    .groups = 'drop'
  ) %>%
  filter(constant) %>%
  select(loop_type) %>%
  mutate(W_statistic = NA, p_value = NA)

# Combine results for log-transformed data
log_shapiro_results <- bind_rows(log_shapiro_results, constant_log_groups)

# Save the Shapiro-Wilk test results for log transformation to a CSV file
write.csv(log_shapiro_results, "memory_log_results.csv", row.names = FALSE)

# Perform square root transformation
df <- df %>%
  mutate(
    sqrt_memory_usage = sqrt(memory_usage)  # Square root-transform memory usage
  )

# Perform the Shapiro-Wilk normality test for square root-transformed data
sqrt_shapiro_results <- df %>%
  group_by(loop_type) %>%
  filter(n_distinct(sqrt_memory_usage) > 1) %>%  # Only include groups with more than one unique value
  summarise(
    sw_test = list(shapiro.test(sqrt_memory_usage)),  # Conduct Shapiro-Wilk test
    .groups = 'drop'
  )

# Extract W-statistic and p-value for square root-transformed data
sqrt_shapiro_results <- sqrt_shapiro_results %>%
  mutate(
    W_statistic = sapply(sw_test, function(x) x$statistic),
    p_value = sapply(sw_test, function(x) x$p.value)
  ) %>%
  select(loop_type, W_statistic, p_value)

# Handle groups with constant values for square root-transformed data
constant_sqrt_groups <- df %>%
  group_by(loop_type) %>%
  summarise(
    constant = n_distinct(sqrt_memory_usage) == 1,
    .groups = 'drop'
  ) %>%
  filter(constant) %>%
  select(loop_type) %>%
  mutate(W_statistic = NA, p_value = NA)

# Combine results for square root-transformed data
sqrt_shapiro_results <- bind_rows(sqrt_shapiro_results, constant_sqrt_groups)

# Save the Shapiro-Wilk test results for square root transformation to a CSV file
write.csv(sqrt_shapiro_results, "memory_sqrt_results.csv", row.names = FALSE)

# Display results (optional)
print("Log Transformation Shapiro-Wilk Results:")
print(log_shapiro_results)

print("Square Root Transformation Shapiro-Wilk Results:")
print(sqrt_shapiro_results)

