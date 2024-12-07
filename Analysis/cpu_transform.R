library(dplyr)

# Load the datasets
df1 <- read.csv("run_table-1.csv")
df2 <- read.csv("run_table-2.csv")

# Combine the two datasets into one
df <- bind_rows(df1, df2)

# Perform log transformation
df <- df %>%
  mutate(
    log_cpu_usage = case_when(
      loop_type == "loop1" ~ log(cpu_usage),
      loop_type == "loop1_opt_cacheblocking" ~ log(cpu_usage),
      loop_type == "loop1_opt_unrolling" ~ log(cpu_usage),
      loop_type == "loop1_opt_batching" ~ log(cpu_usage),
      loop_type == "loop2" ~ log(cpu_usage),
      loop_type == "loop2_opt_cacheblocking" ~ log(cpu_usage),
      loop_type == "loop2_opt_unrolling" ~ log(cpu_usage),
      loop_type == "loop2_opt_batching" ~ log(cpu_usage),
      loop_type == "loop3" ~ log(cpu_usage),
      loop_type == "loop3_opt_cacheblocking" ~ log(cpu_usage),
      loop_type == "loop3_opt_unrolling" ~ log(cpu_usage),
      loop_type == "loop3_opt_batching" ~ log(cpu_usage),
      loop_type == "loop4" ~ log(cpu_usage),
      loop_type == "loop4_opt_cacheblocking" ~ log(cpu_usage),
      loop_type == "loop4_opt_unrolling" ~ log(cpu_usage),
      loop_type == "loop4_opt_batching" ~ log(cpu_usage),
      loop_type == "loop5" ~ log(cpu_usage),
      loop_type == "loop5_opt_cacheblocking" ~ log(cpu_usage),
      loop_type == "loop5_opt_unrolling" ~ log(cpu_usage),
      loop_type == "loop5_opt_batching" ~ log(cpu_usage),
      loop_type == "loop6" ~ log(cpu_usage),
      loop_type == "loop6_opt_cacheblocking" ~ log(cpu_usage),
      loop_type == "loop6_opt_unrolling" ~ log(cpu_usage),
      loop_type == "loop6_opt_batching" ~ log(cpu_usage),
      loop_type == "loop7" ~ log(cpu_usage),
      loop_type == "loop7_opt_cacheblocking" ~ log(cpu_usage),
      loop_type == "loop7_opt_unrolling" ~ log(cpu_usage),
      loop_type == "loop7_opt_batching" ~ log(cpu_usage),
      loop_type == "loop8" ~ log(cpu_usage),
      loop_type == "loop8_opt_cacheblocking" ~ log(cpu_usage),
      loop_type == "loop8_opt_unrolling" ~ log(cpu_usage),
      loop_type == "loop8_opt_batching" ~ log(cpu_usage),
      loop_type == "loop9" ~ log(cpu_usage),
      loop_type == "loop9_opt_cacheblocking" ~ log(cpu_usage),
      loop_type == "loop9_opt_unrolling" ~ log(cpu_usage),
      loop_type == "loop9_opt_batching" ~ log(cpu_usage),
      loop_type == "loop10" ~ log(cpu_usage),
      loop_type == "loop10_opt_cacheblocking" ~ log(cpu_usage),
      loop_type == "loop10_opt_unrolling" ~ log(cpu_usage),
      loop_type == "loop10_opt_batching" ~ log(cpu_usage)
    )
  )

# Perform the Shapiro-Wilk normality test
shapiro_results <- df %>%
  group_by(loop_type) %>%
  summarise(
    sw_test = list(shapiro.test(log_cpu_usage)),  # Conduct the Shapiro-Wilk test on the log-transformed data
    .groups = 'drop'
  )

# Extract W-statistic and p-value from the Shapiro-Wilk test results
shapiro_results <- shapiro_results %>%
  mutate(
    W_statistic = sapply(sw_test, function(x) x$statistic),
    p_value = sapply(sw_test, function(x) x$p.value)
  ) %>%
  select(loop_type, W_statistic, p_value)

# Save the Shapiro-Wilk test results to a CSV file
write.csv(shapiro_results, "cpu_log_results.csv", row.names = FALSE)


#===================================================================================
#===================================================================================
#===================================================================================

# Perform square root transformation
df <- df %>%
  mutate(
    sqrt_cpu_usage = case_when(
      loop_type == "loop1" ~ sqrt(cpu_usage),
      loop_type == "loop1_opt_cacheblocking" ~ sqrt(cpu_usage),
      loop_type == "loop1_opt_unrolling" ~ sqrt(cpu_usage),
      loop_type == "loop1_opt_batching" ~ sqrt(cpu_usage),
      loop_type == "loop2" ~ sqrt(cpu_usage),
      loop_type == "loop2_opt_cacheblocking" ~ sqrt(cpu_usage),
      loop_type == "loop2_opt_unrolling" ~ sqrt(cpu_usage),
      loop_type == "loop2_opt_batching" ~ sqrt(cpu_usage),
      loop_type == "loop3" ~ sqrt(cpu_usage),
      loop_type == "loop3_opt_cacheblocking" ~ sqrt(cpu_usage),
      loop_type == "loop3_opt_unrolling" ~ sqrt(cpu_usage),
      loop_type == "loop3_opt_batching" ~ sqrt(cpu_usage),
      loop_type == "loop4" ~ sqrt(cpu_usage),
      loop_type == "loop4_opt_cacheblocking" ~ sqrt(cpu_usage),
      loop_type == "loop4_opt_unrolling" ~ sqrt(cpu_usage),
      loop_type == "loop4_opt_batching" ~ sqrt(cpu_usage),
      loop_type == "loop5" ~ sqrt(cpu_usage),
      loop_type == "loop5_opt_cacheblocking" ~ sqrt(cpu_usage),
      loop_type == "loop5_opt_unrolling" ~ sqrt(cpu_usage),
      loop_type == "loop5_opt_batching" ~ sqrt(cpu_usage),
      loop_type == "loop6" ~ sqrt(cpu_usage),
      loop_type == "loop6_opt_cacheblocking" ~ sqrt(cpu_usage),
      loop_type == "loop6_opt_unrolling" ~ sqrt(cpu_usage),
      loop_type == "loop6_opt_batching" ~ sqrt(cpu_usage),
      loop_type == "loop7" ~ sqrt(cpu_usage),
      loop_type == "loop7_opt_cacheblocking" ~ sqrt(cpu_usage),
      loop_type == "loop7_opt_unrolling" ~ sqrt(cpu_usage),
      loop_type == "loop7_opt_batching" ~ sqrt(cpu_usage),
      loop_type == "loop8" ~ sqrt(cpu_usage),
      loop_type == "loop8_opt_cacheblocking" ~ sqrt(cpu_usage),
      loop_type == "loop8_opt_unrolling" ~ sqrt(cpu_usage),
      loop_type == "loop8_opt_batching" ~ sqrt(cpu_usage),
      loop_type == "loop9" ~ sqrt(cpu_usage),
      loop_type == "loop9_opt_cacheblocking" ~ sqrt(cpu_usage),
      loop_type == "loop9_opt_unrolling" ~ sqrt(cpu_usage),
      loop_type == "loop9_opt_batching" ~ sqrt(cpu_usage),
      loop_type == "loop10" ~ sqrt(cpu_usage),
      loop_type == "loop10_opt_cacheblocking" ~ sqrt(cpu_usage),
      loop_type == "loop10_opt_unrolling" ~ sqrt(cpu_usage),
      loop_type == "loop10_opt_batching" ~ sqrt(cpu_usage)
    )
  )

# Perform the Shapiro-Wilk normality test
shapiro_results <- df %>%
  group_by(loop_type) %>%
  summarise(
    sw_test = list(shapiro.test(sqrt_cpu_usage)),  # Conduct the Shapiro-Wilk test on the sqrt-transformed data
    .groups = 'drop'
  )

# Extract W-statistic and p-value from the Shapiro-Wilk test results
shapiro_results <- shapiro_results %>%
  mutate(
    W_statistic = sapply(sw_test, function(x) x$statistic),
    p_value = sapply(sw_test, function(x) x$p.value)
  ) %>%
  select(loop_type, W_statistic, p_value)

# Save the Shapiro-Wilk test results to a CSV file
write.csv(shapiro_results, "cpu_square_results.csv", row.names = FALSE)
