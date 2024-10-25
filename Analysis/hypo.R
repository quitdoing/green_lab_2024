# 


csv_files <- c("run_table1-4.csv", "run_table5-8.csv", "run_table9-13.csv","run_table_yes1-4.csv", "run_table_yes5-8.csv", "run_table_yes9-13.csv")

# 
data_list <- lapply(csv_files, read.csv)

# 
loop_data <- do.call(rbind, data_list)

# filter for "looptype" columns
fusion_rows <- loop_data[grepl("breaking", loop_data$loop_type), ]

cor_result_pearson1 <- cor(fusion_rows$energy_usage, fusion_rows$cpu_usage, method = "pearson")

#
cor_result_spearman2 <- cor(fusion_rows$energy_usage, fusion_rows$cpu_usage, method = "spearman")

cor_result_pearson3 <- cor(fusion_rows$energy_usage, fusion_rows$memory_usage, method = "pearson")

# 
cor_result_spearman4 <- cor(fusion_rows$energy_usage, fusion_rows$memory_usage, method = "spearman")

# 
cor_result_pearson5 <- cor(fusion_rows$energy_usage, fusion_rows$execution_time, method = "pearson")

# 
cor_result_spearman6 <- cor(fusion_rows$energy_usage, fusion_rows$execution_time, method = "spearman")

print(cor_result_pearson1)

print(cor_result_spearman2)

print(cor_result_pearson3)

print(cor_result_spearman4)

print(cor_result_pearson5)

print(cor_result_spearman6)

