library(ggplot2)
library(dplyr)

# Read CSV files
df1 <- read.csv("run_table-1.csv")
df2 <- read.csv("run_table-2.csv")

# Combine the two data frames
df <- bind_rows(df1, df2)

# Clean data by removing rows with NA values
df_clean <- df %>%
  filter(!is.na(cpu_usage) & !is.na(energy_usage))

# Filter data for the batching optimization method
df_batching <- df_clean %>%
  filter(grepl("batching", loop_type))  # Select rows where "loop_type" contains "batching"

# Plot scatter plot and regression line for the batching optimization
ggplot(df_batching, aes(x = energy_usage, y = cpu_usage)) +
  geom_point() +  # Create a scatter plot
  geom_smooth(method = "lm", color = "red") +  # Add a linear regression line
  labs(title = "Energy Usage vs CPU Usage (Batching Optimization)",
       x = "Energy Usage",
       y = "CPU Usage") +
  theme_minimal()

# Save the plot as a PNG file
ggsave("batching_energy_vs_cpu_usage.png", width = 8, height = 6, dpi = 300)

# Compute Spearman correlation
correlation <- cor(df_batching$energy_usage, df_batching$cpu_usage, method = "spearman")
print(paste("Spearman correlation for batching: ", correlation))

# Perform significance testing using cor.test()
spearman_test <- cor.test(df_batching$energy_usage, df_batching$cpu_usage, method = "spearman")
print(spearman_test)

# ==============================================================================================================
# Filter data for the cacheblocking optimization method
df_cacheblocking <- df_clean %>%
  filter(grepl("cacheblocking", loop_type))  # Select rows where "loop_type" contains "cacheblocking"

# Plot scatter plot and regression line for the cacheblocking optimization
ggplot(df_cacheblocking, aes(x = energy_usage, y = cpu_usage)) +
  geom_point() +  # Create a scatter plot
  geom_smooth(method = "lm", color = "red") +  # Add a linear regression line
  labs(title = "Energy Usage vs CPU Usage (Cacheblocking Optimization)",
       x = "Energy Usage",
       y = "CPU Usage") +
  theme_minimal()

# Save the plot as a PNG file
ggsave("cacheblocking_energy_vs_cpu_usage.png", width = 8, height = 6, dpi = 300)

# Compute Spearman correlation
correlation <- cor(df_cacheblocking$energy_usage, df_cacheblocking$cpu_usage, method = "spearman")
print(paste("Spearman correlation for cacheblocking: ", correlation))

# Perform significance testing using cor.test()
spearman_test <- cor.test(df_cacheblocking$energy_usage, df_cacheblocking$cpu_usage, method = "spearman")
print(spearman_test)

# ==============================================================================================================
# Filter data for the unrolling optimization method
df_unrolling <- df_clean %>%
  filter(grepl("unrolling", loop_type))  # Select rows where "loop_type" contains "unrolling"

# Plot scatter plot and regression line for the unrolling optimization
ggplot(df_unrolling, aes(x = energy_usage, y = cpu_usage)) +
  geom_point() +  # Create a scatter plot
  geom_smooth(method = "lm", color = "red") +  # Add a linear regression line
  labs(title = "Energy Usage vs CPU Usage (Unrolling Optimization)",
       x = "Energy Usage",
       y = "CPU Usage") +
  theme_minimal()

# Save the plot as a PNG file
ggsave("unrolling_energy_vs_cpu_usage.png", width = 8, height = 6, dpi = 300)

# Compute Spearman correlation
correlation <- cor(df_unrolling$energy_usage, df_unrolling$cpu_usage, method = "spearman")
print(paste("Spearman correlation for unrolling: ", correlation))

# Perform significance testing using cor.test()
spearman_test <- cor.test(df_unrolling$energy_usage, df_unrolling$cpu_usage, method = "spearman")
print(spearman_test)
