
csv_files <- c("run_table1-4.csv", "run_table5-8.csv", "run_table9-13.csv","run_table_yes1-4.csv", "run_table_yes5-8.csv", "run_table_yes9-13.csv")


data_list <- lapply(csv_files, read.csv)


loop_data <- do.call(rbind, data_list)


fusion_rows <- loop_data[grepl("unrolling", loop_data$loop_type), ]


par(mfrow = c(3, 1))

par(bg = "whitesmoke")


plot(fusion_rows$energy_usage, fusion_rows$execution_time,
     xlab = "Energy Usage (Joules)",
     ylab = "Execution Time (s)",
     main = "Energy Usage vs Execution Time (unrolling)",
     col = "blue",
     pch = 19)

plot(fusion_rows$energy_usage, fusion_rows$cpu_usage,
     xlab = "Energy Usage (Joules)",
     ylab = "CPU Usage (%)",
     main = "Energy Usage vs CPU Usage (unrolling)",
     col = "green",
     pch = 19)


plot(fusion_rows$energy_usage, fusion_rows$memory_usage,
     xlab = "Energy Usage (Joules)",
     ylab = "Memory Usage (MB)",
     main = "Energy Usage vs Memory Usage (unrolling)",
     col = "red",
     pch = 19)


par(mfrow = c(1, 1))

