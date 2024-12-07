library(ggplot2)
library(dplyr)

# Read the CSV files
df1 <- read.csv("run_table-1.csv")
df2 <- read.csv("run_table-2.csv")

# Combine the two data frames
df <- bind_rows(df1, df2)

# Clean the data by removing rows with NA values
df_clean <- df %>%
  filter(!is.na(execution_time) & !is.na(energy_usage))

# Filter data for batching optimization method
df_batching <- df_clean %>%
  filter(grepl("batching", loop_type))  # Only select rows with "batching" in loop_type

# Plot scatter plot and regression line for batching optimization method
ggplot(df_batching, aes(x = energy_usage, y = execution_time)) +
  geom_point() +  # Plot scatter points
  geom_smooth(method = "lm", color = "red") +  # Add linear regression line
  labs(title = "Energy Usage vs Execution Time (Batching Optimization)",
       x = "Energy Usage",
       y = "Execution Time") +
  theme_minimal()

# Save the plot as a PNG file
ggsave("batching_energy_vs_execution_time.png", width = 8, height = 6, dpi = 300)

# Calculate Spearman correlation
correlation <- cor(df_batching$energy_usage, df_batching$execution_time, method = "spearman")
print(paste("Spearman correlation for batching: ", correlation))

# Alternatively, perform a significance test using cor.test()
spearman_test <- cor.test(df_batching$energy_usage, df_batching$execution_time, method = "spearman")
print(spearman_test)

#===============================================================================================================
#===============================================================================================================
#===============================================================================================================
#===============================================================================================================

# Filter data for cache blocking optimization method
df_cacheblocking <- df_clean %>%
  filter(grepl("cacheblocking", loop_type))  # Only select rows with "cacheblocking" in loop_type

# Plot scatter plot and regression line for cache blocking optimization method
ggplot(df_cacheblocking, aes(x = energy_usage, y = execution_time)) +
  geom_point() +  # Plot scatter points
  geom_smooth(method = "lm", color = "red") +  # Add linear regression line
  labs(title = "Energy Usage vs Execution Time (Cache Blocking Optimization)",
       x = "Energy Usage",
       y = "Execution Time") +
  theme_minimal()

# Save the plot as a PNG file
ggsave("cacheblocking_energy_vs_execution_time.png", width = 8, height = 6, dpi = 300)

# Calculate Spearman correlation
correlation <- cor(df_cacheblocking$energy_usage, df_cacheblocking$execution_time, method = "spearman")
print(paste("Spearman correlation for cacheblocking: ", correlation))

# Alternatively, perform a significance test using cor.test()
spearman_test <- cor.test(df_cacheblocking$energy_usage, df_cacheblocking$execution_time, method = "spearman")
print(spearman_test)

#===============================================================================================================
#===============================================================================================================
#===============================================================================================================
#===============================================================================================================

# Filter data for unrolling optimization method
df_unrolling <- df_clean %>%
  filter(grepl("unrolling", loop_type))  # Only select rows with "unrolling" in loop_type

# Plot scatter plot and regression line for unrolling optimization method
ggplot(df_unrolling, aes(x = energy_usage, y = execution_time)) +
  geom_point() +  # Plot scatter points
  geom_smooth(method = "lm", color = "red") +  # Add linear regression line
  labs(title = "Energy Usage vs Execution Time (Unrolling Optimization)",
       x = "Energy Usage",
       y = "Execution Time") +
  theme_minimal()

# Save the plot as a PNG file
ggsave("unrolling_energy_vs_execution_time.png", width = 8, height = 6, dpi = 300)

# Calculate Spearman correlation
correlation <- cor(df_unrolling$energy_usage, df_unrolling$execution_time, method = "spearman")
print(paste("Spearman correlation for unrolling: ", correlation))

# Alternatively, perform a significance test using cor.test()
spearman_test <- cor.test(df_unrolling$energy_usage, df_unrolling$execution_time, method = "spearman")
print(spearman_test)
