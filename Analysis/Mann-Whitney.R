# Initialize an empty data frame to store the results
results_df <- data.frame(
  loop_type1 = character(),
  loop_type2 = character(),
  W_statistic = numeric(),
  p_value = numeric(),
  stringsAsFactors = FALSE
)

# Loop through each loop and optimization method
for (loop_number in loop_numbers) {
  # Get original loop data
  loop_data <- df[df$loop_type == paste("loop", loop_number, sep = ""), "energy_usage"]
  
  # For each optimization method, perform Mann-Whitney U test
  for (method in optimization_methods) {
    # Get optimized loop data
    optimized_loop_data <- df[df$loop_type == paste("loop", loop_number, "_", method, sep = ""), "energy_usage"]
    
    # Perform Mann-Whitney U test with exact = FALSE
    result <- wilcox.test(loop_data, optimized_loop_data, exact = FALSE)
    
    # Store the results in the data frame
    results_df <- rbind(results_df, data.frame(
      loop_type1 = paste("loop", loop_number, sep = ""),
      loop_type2 = paste("loop", loop_number, "_", method, sep = ""),
      W_statistic = result$statistic,
      p_value = result$p.value
    ))
  }
}

# Save the results to a CSV file
write.csv(results_df, "mann_whitney_results.csv", row.names = FALSE)


