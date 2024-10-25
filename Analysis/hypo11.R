# 加载必要的包

# 加载必要的包
library(dplyr)

# 读取CSV文件并合并
csv_files <- c("run_table9-13.csv", "run_table_yes9-13.csv")
data_list <- lapply(csv_files, read.csv)
loop_data <- do.call(rbind, data_list)

# 筛选优化前和优化后的数据
original_data <- subset(loop_data, loop_type == "loop13")$energy_usage
optimized_data <- subset(loop_data, loop_type == "loop13_opt_fusion")$energy_usage

# 进行Mann-Whitney U检验
if (length(original_data) > 0 & length(optimized_data) > 0) {
  wilcox_result <- wilcox.test(original_data, optimized_data, exact = FALSE)
  print(paste("Loop Type: loop1 - W-value:", wilcox_result$statistic))
  print(paste("Loop Type: loop1 - P-value:", wilcox_result$p.value))

