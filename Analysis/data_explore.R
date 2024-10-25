
data1 <- read.csv("run_table5-8.csv")
data2 <- read.csv("run_table_yes5-8.csv")

loop6_data <- subset(data1, loop_type == "loop6")
loop6_data1 <- subset(data2, loop_type == "loop6_opt_cacheblocking")
loop6_data2 <- subset(data2, loop_type == "loop6_opt_predicate")
loop6_data3 <- subset(data2, loop_type == "loop6_opt_collapsing")
loop6_data4 <- subset(data2, loop_type == "loop6_opt_unrolling")


mean_energy1 <- median(loop6_data$energy_usage, na.rm = TRUE)
mean_energy2 <- median(loop6_data1$energy_usage, na.rm = TRUE)
mean_energy3 <- median(loop6_data2$energy_usage, na.rm = TRUE)
mean_energy4 <- mean(loop6_data3$energy_usage, na.rm = TRUE)
mean_energy5 <- median(loop6_data4$energy_usage, na.rm = TRUE)


mean_execution_time1 <- median(loop6_data$execution_time, na.rm = TRUE)
mean_execution_time2 <- median(loop6_data1$execution_time, na.rm = TRUE)
mean_execution_time3 <- median(loop6_data2$execution_time, na.rm = TRUE)
mean_execution_time4 <- mean(loop6_data3$execution_time, na.rm = TRUE)
mean_execution_time5 <- median(loop6_data4$execution_time, na.rm = TRUE)

print(mean_energy1)
print(mean_energy2)
print(mean_energy3)
print(mean_energy4)
print(mean_energy5)

print(mean_execution_time1)
print(mean_execution_time2)
print(mean_execution_time3)
print(mean_execution_time4)
print(mean_execution_time5)

