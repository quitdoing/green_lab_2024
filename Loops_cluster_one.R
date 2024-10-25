
library(ggplot2)
library(dplyr)
library(stringr)


data_original <- read.csv("run_table5-8.csv")
data_optimized <- read.csv("run_table_yes5-8.csv")


data_original <- data_original %>%
  mutate(optimization_method = "No Optimization",
         loop_type_clean = loop_type)  


data_optimized <- data_optimized %>%
  mutate(
    optimization_method = str_extract(loop_type, "opt_[a-zA-Z]+"),  
    loop_type_clean = str_extract(loop_type, "loop[0-9]+")  
  )


combined_data <- rbind(data_original, data_optimized)


specific_loop <- "loop6"


filtered_data <- combined_data %>%
  filter(loop_type_clean == specific_loop)


ggplot(filtered_data, aes(x = optimization_method, y = energy_usage, fill = optimization_method)) +
  geom_violin(alpha = 0.7, width = 1, trim = FALSE) +  # 小提琴图
  geom_boxplot(width = 0.1, alpha = 0.7, color = "black", notch = TRUE) +  # 叠加箱线图
  ggtitle(paste("Energy Usage for", specific_loop, "by Optimization Method")) +
  xlab("Optimization Method") +
  ylab("Energy Usage") +
  theme_minimal(base_size = 14) +
  scale_fill_manual(values = c("#F8766D", "#00BFC4", "#A3A500", "#E76BF3","#00FFFF")) +
  theme(
    plot.title = element_text(hjust = 0.5, face = "bold", size = 20),
    axis.title = element_text(face = "bold"),
    legend.title = element_text(face = "bold",size = 10),
    legend.position = "top"
  ) +
  coord_flip()   
