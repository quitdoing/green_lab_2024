# Install and load the effsize package if not already installed
library(effsize)

# Example for calculating Cliff's Delta for all loops
df1 <- read.csv("run_table-1.csv")
df2 <- read.csv("run_table-2.csv")

df <- bind_rows(df1, df2)  # Combine the original and optimized data
# Assuming df contains 'loop_type' and 'energy_usage' columns

# Initialize an empty list to store the results
cliffs_delta_results <- list()

# Loop through each loop (loop1 to loop10)
for (i in 1:10) {
  # Extract the data for the current loop and its optimized versions
  loop_data <- df[df$loop_type == paste("loop", i, sep=""), "energy_usage"]
  loop_opt_cacheblocking_data <- df[df$loop_type == paste("loop", i, "_opt_cacheblocking", sep=""), "energy_usage"]
  loop_opt_unrolling_data <- df[df$loop_type == paste("loop", i, "_opt_unrolling", sep=""), "energy_usage"]
  loop_opt_batching_data <- df[df$loop_type == paste("loop", i, "_opt_batching", sep=""), "energy_usage"]
  
  # Calculate Cliff's Delta for the current loop and its optimizations
  cliffs_delta_cacheblocking <- cliff.delta(loop_data, loop_opt_cacheblocking_data)
  cliffs_delta_unrolling <- cliff.delta(loop_data, loop_opt_unrolling_data)
  cliffs_delta_batching <- cliff.delta(loop_data, loop_opt_batching_data)
  
  # Store the results in a list
  cliffs_delta_results[[i]] <- data.frame(
    loop_type1 = paste("loop", i, sep=""),
    loop_type2_cacheblocking = paste("loop", i, "_opt_cacheblocking", sep=""),
    delta_cacheblocking = cliffs_delta_cacheblocking$estimate,
    ci_lower_cacheblocking = cliffs_delta_cacheblocking$conf.int[1],
    ci_upper_cacheblocking = cliffs_delta_cacheblocking$conf.int[2],
    
    loop_type2_unrolling = paste("loop", i, "_opt_unrolling", sep=""),
    delta_unrolling = cliffs_delta_unrolling$estimate,
    ci_lower_unrolling = cliffs_delta_unrolling$conf.int[1],
    ci_upper_unrolling = cliffs_delta_unrolling$conf.int[2],
    
    loop_type2_batching = paste("loop", i, "_opt_batching", sep=""),
    delta_batching = cliffs_delta_batching$estimate,
    ci_lower_batching = cliffs_delta_batching$conf.int[1],
    ci_upper_batching = cliffs_delta_batching$conf.int[2]
  )
}

# Combine all the data frames into a single data frame
final_results <- do.call(rbind, cliffs_delta_results)

# Write the results to a CSV file
write.csv(final_results, "cliffs_delta_results.csv", row.names = FALSE)

# Optionally, print the results to check
print(final_results)

