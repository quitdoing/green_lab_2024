library(dplyr)

# Load the datasets
df1 <- read.csv("run_table-1.csv")
df2 <- read.csv("run_table-2.csv")

# Combine the two datasets into one
df <- bind_rows(df1, df2)

# Perform log transformation
df <- df %>%
  mutate(
    log_energy_usage = case_when(
      loop_type == "loop1" ~ log(energy_usage),  # Apply log transformation to loop1
      loop_type == "loop1_opt_cacheblocking" ~ log(energy_usage),  # Apply log transformation to loop1_opt_cacheblocking
      loop_type == "loop1_opt_unrolling" ~ log(energy_usage),  # Apply log transformation to loop1_opt_unrolling
      loop_type == "loop1_opt_batching" ~ log(energy_usage),  # Apply log transformation to loop1_opt_batching
      loop_type == "loop2" ~ log(energy_usage),  # Apply log transformation to loop2
      loop_type == "loop2_opt_cacheblocking" ~ log(energy_usage),  # Apply log transformation to loop2_opt_cacheblocking
      loop_type == "loop2_opt_unrolling" ~ log(energy_usage),  # Apply log transformation to loop2_opt_unrolling
      loop_type == "loop2_opt_batching" ~ log(energy_usage),  # Apply log transformation to loop2_opt_batching
      loop_type == "loop3" ~ log(energy_usage),  # Apply log transformation to loop3
      loop_type == "loop3_opt_cacheblocking" ~ log(energy_usage),  # Apply log transformation to loop3_opt_cacheblocking
      loop_type == "loop3_opt_unrolling" ~ log(energy_usage),  # Apply log transformation to loop3_opt_unrolling
      loop_type == "loop3_opt_batching" ~ log(energy_usage),  # Apply log transformation to loop3_opt_batching
      loop_type == "loop4" ~ log(energy_usage),  # Apply log transformation to loop4
      loop_type == "loop4_opt_cacheblocking" ~ log(energy_usage),  # Apply log transformation to loop4_opt_cacheblocking
      loop_type == "loop4_opt_unrolling" ~ log(energy_usage),  # Apply log transformation to loop4_opt_unrolling
      loop_type == "loop4_opt_batching" ~ log(energy_usage),  # Apply log transformation to loop4_opt_batching
      loop_type == "loop5" ~ log(energy_usage),  # Apply log transformation to loop5
      loop_type == "loop5_opt_cacheblocking" ~ log(energy_usage),  # Apply log transformation to loop5_opt_cacheblocking
      loop_type == "loop5_opt_unrolling" ~ log(energy_usage),  # Apply log transformation to loop5_opt_unrolling
      loop_type == "loop5_opt_batching" ~ log(energy_usage),  # Apply log transformation to loop5_opt_batching
      loop_type == "loop6" ~ log(energy_usage),  # Apply log transformation to loop6
      loop_type == "loop6_opt_cacheblocking" ~ log(energy_usage),  # Apply log transformation to loop6_opt_cacheblocking
      loop_type == "loop6_opt_unrolling" ~ log(energy_usage),  # Apply log transformation to loop6_opt_unrolling
      loop_type == "loop6_opt_batching" ~ log(energy_usage),  # Apply log transformation to loop6_opt_batching
      loop_type == "loop7" ~ log(energy_usage),  # Apply log transformation to loop7
      loop_type == "loop7_opt_cacheblocking" ~ log(energy_usage),  # Apply log transformation to loop7_opt_cacheblocking
      loop_type == "loop7_opt_unrolling" ~ log(energy_usage),  # Apply log transformation to loop7_opt_unrolling
      loop_type == "loop7_opt_batching" ~ log(energy_usage),  # Apply log transformation to loop7_opt_batching
      loop_type == "loop8" ~ log(energy_usage),  # Apply log transformation to loop8
      loop_type == "loop8_opt_cacheblocking" ~ log(energy_usage),  # Apply log transformation to loop8_opt_cacheblocking
      loop_type == "loop8_opt_unrolling" ~ log(energy_usage),  # Apply log transformation to loop8_opt_unrolling
      loop_type == "loop8_opt_batching" ~ log(energy_usage),  # Apply log transformation to loop8_opt_batching
      loop_type == "loop9" ~ log(energy_usage),  # Apply log transformation to loop9
      loop_type == "loop9_opt_cacheblocking" ~ log(energy_usage),  # Apply log transformation to loop9_opt_cacheblocking
      loop_type == "loop9_opt_unrolling" ~ log(energy_usage),  # Apply log transformation to loop9_opt_unrolling
      loop_type == "loop9_opt_batching" ~ log(energy_usage),  # Apply log transformation to loop9_opt_batching
      loop_type == "loop10" ~ log(energy_usage),  # Apply log transformation to loop10
      loop_type == "loop10_opt_cacheblocking" ~ log(energy_usage),  # Apply log transformation to loop10_opt_cacheblocking
      loop_type == "loop10_opt_unrolling" ~ log(energy_usage),  # Apply log transformation to loop10_opt_unrolling
      loop_type == "loop10_opt_batching" ~ log(energy_usage)   # Apply log transformation to loop10_opt_batching
    )
  )

# Perform the Shapiro-Wilk normality test
shapiro_results <- df %>%
  group_by(loop_type) %>%
  summarise(
    sw_test = list(shapiro.test(log_energy_usage)),  # Conduct the Shapiro-Wilk test on the log-transformed data
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
write.csv(shapiro_results, "energy_log_results.csv", row.names = FALSE)

# Display the results
#print(shapiro_results)



#===================================================================================
#===================================================================================
#===================================================================================


# Perform square root transformation
df <- df %>%
  mutate(
    sqrt_energy_usage = case_when(
      loop_type == "loop1" ~ sqrt(energy_usage),
      loop_type == "loop1_opt_cacheblocking" ~ sqrt(energy_usage),
      loop_type == "loop1_opt_unrolling" ~ sqrt(energy_usage),
      loop_type == "loop1_opt_batching" ~ sqrt(energy_usage),
      loop_type == "loop2" ~ sqrt(energy_usage),
      loop_type == "loop2_opt_cacheblocking" ~ sqrt(energy_usage),
      loop_type == "loop2_opt_unrolling" ~ sqrt(energy_usage),
      loop_type == "loop2_opt_batching" ~ sqrt(energy_usage),
      loop_type == "loop3" ~ sqrt(energy_usage),
      loop_type == "loop3_opt_cacheblocking" ~ sqrt(energy_usage),
      loop_type == "loop3_opt_unrolling" ~ sqrt(energy_usage),
      loop_type == "loop3_opt_batching" ~ sqrt(energy_usage),
      loop_type == "loop4" ~ sqrt(energy_usage),
      loop_type == "loop4_opt_cacheblocking" ~ sqrt(energy_usage),
      loop_type == "loop4_opt_unrolling" ~ sqrt(energy_usage),
      loop_type == "loop4_opt_batching" ~ sqrt(energy_usage),
      loop_type == "loop5" ~ sqrt(energy_usage),
      loop_type == "loop5_opt_cacheblocking" ~ sqrt(energy_usage),
      loop_type == "loop5_opt_unrolling" ~ sqrt(energy_usage),
      loop_type == "loop5_opt_batching" ~ sqrt(energy_usage),
      loop_type == "loop6" ~ sqrt(energy_usage),
      loop_type == "loop6_opt_cacheblocking" ~ sqrt(energy_usage),
      loop_type == "loop6_opt_unrolling" ~ sqrt(energy_usage),
      loop_type == "loop6_opt_batching" ~ sqrt(energy_usage),
      loop_type == "loop7" ~ sqrt(energy_usage),
      loop_type == "loop7_opt_cacheblocking" ~ sqrt(energy_usage),
      loop_type == "loop7_opt_unrolling" ~ sqrt(energy_usage),
      loop_type == "loop7_opt_batching" ~ sqrt(energy_usage),
      loop_type == "loop8" ~ sqrt(energy_usage),
      loop_type == "loop8_opt_cacheblocking" ~ sqrt(energy_usage),
      loop_type == "loop8_opt_unrolling" ~ sqrt(energy_usage),
      loop_type == "loop8_opt_batching" ~ sqrt(energy_usage),
      loop_type == "loop9" ~ sqrt(energy_usage),
      loop_type == "loop9_opt_cacheblocking" ~ sqrt(energy_usage),
      loop_type == "loop9_opt_unrolling" ~ sqrt(energy_usage),
      loop_type == "loop9_opt_batching" ~ sqrt(energy_usage),
      loop_type == "loop10" ~ sqrt(energy_usage),
      loop_type == "loop10_opt_cacheblocking" ~ sqrt(energy_usage),
      loop_type == "loop10_opt_unrolling" ~ sqrt(energy_usage),
      loop_type == "loop10_opt_batching" ~ sqrt(energy_usage)
    )
  )

# Perform the Shapiro-Wilk normality test
shapiro_results <- df %>%
  group_by(loop_type) %>%
  summarise(
    sw_test = list(shapiro.test(sqrt_energy_usage)),  # Conduct the Shapiro-Wilk test on the sqrt-transformed data
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
write.csv(shapiro_results, "energy_sqrt_results.csv", row.names = FALSE)


