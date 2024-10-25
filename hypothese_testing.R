# 导入数据
# 读取数据
csv_files <- c("run_table1-4.csv", "run_table5-8.csv", "run_table9-13.csv","run_table_yes1-4.csv", "run_table_yes5-8.csv", "run_table_yes9-13.csv")

# 读取所有指定的 CSV 文件并存储在一个列表中
data_list <- lapply(csv_files, read.csv)

# 将所有数据框合并成一个大的数据框
loop_data <- do.call(rbind, data_list)

# 查看数据结构，确定列名
str(loop_data)

# 假设有两列，分别为 loop_type 和 energy_usage
# 提取不同 loop 的能量消耗数据，并进行正态性检验
unique_loops <- unique(loop_data$loop_type)

for (loop in unique_loops) {
  # 提取对应 loop 的数据
 loop_data1 <- subset(loop_data, loop_type == loop)$energy_usage
  
  
  
  # 进行 Shapiro-Wilk 正态性检验
  shapiro_result <- shapiro.test(loop_data1)
  
  # 打印 loop 类型及其对应的 p 值
  
  #print(paste("Loop:", loop, " - p-value:", shapiro_result$p.value))
  
  # 判断数据是否符合正态分布
  if (shapiro_result$p.value > 0.05) {
    print("yes")
  } else {
    print("The data does not conform to a normal distribution")
  }
}

