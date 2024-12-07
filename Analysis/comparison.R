# Create a function to process each loop and generate boxplots with summary stats
generate_plots <- function(loop_number) {
  # Filter the original data for the specific loop
  df_loop <- df_original %>% 
    filter(grepl(paste("^loop", loop_number, "$", sep = ""), loop_type))
  
  # Filter the optimized data for the specific loop
  df_optimized_loop <- df_optimized %>%
    filter(grepl(paste("loop", loop_number, sep = ""), loop_type))
  
  # Add loop_type column to the optimized data
  df_optimized_loop <- df_optimized_loop %>%
    mutate(loop_type = rep(c(
      paste("loop", loop_number, "_opt_cacheblocking", sep = ""),
      paste("loop", loop_number, "_opt_unrolling", sep = ""),
      paste("loop", loop_number, "_opt_batching", sep = "")
    ), each = nrow(df_optimized_loop) / 3))
  
  # Combine original and optimized data for the specific loop
  df_all <- bind_rows(df_loop, df_optimized_loop)
  
  # Convert the data into long format for easy faceting
  df_long <- df_all %>%
    gather(key = "metric", value = "value", execution_time, memory_usage, cpu_usage, energy_usage)
  
  # Print summary statistics for each metric
  print(paste("Summary statistics for loop", loop_number))
  
  for (metric in unique(df_long$metric)) {
    metric_data <- df_long$value[df_long$metric == metric]
    print(paste("Metric:", metric))
    print(summary(metric_data))  # Summary for quartiles, min, max, etc.
    
    # Get boxplot statistics (including outliers)
    box_stats <- boxplot.stats(metric_data)
    print(paste("Min:", box_stats$stats[1]))
    print(paste("Q1:", box_stats$stats[2]))
    print(paste("Median:", box_stats$stats[3]))
    print(paste("Q3:", box_stats$stats[4]))
    print(paste("Max:", box_stats$stats[5]))
    print("Outliers:")
    print(box_stats$out)  # Display outliers
  }
  
  # Plot the boxplots for all metrics in a single plot using faceting
  p <- ggplot(df_long, aes(x = loop_type, y = value, fill = loop_type)) +
    geom_boxplot() +
    facet_wrap(~ metric, scales = "free_y") +  # Create separate panels for each metric
    theme(axis.text.x = element_text(angle = 45, hjust = 1))  # Rotate x-axis labels
  
  # Save the plot to a file (e.g., PNG or PDF)
  ggsave(paste("loop", loop_number, "_boxplots.png", sep = ""), plot = p, width = 8, height = 6, dpi = 300)
}

# Loop through each loop (1 to 10) and generate and save the corresponding plots
for (i in 1:10) {
  generate_plots(i)
}
