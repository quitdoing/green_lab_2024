
df1 <- read.csv("run_table-1.csv")
df2 <- read.csv("run_table-2.csv")

df <- bind_rows(df1, df2)


loop_types <- unique(df$loop_type)  

print(loop_types)

png("energy_qq_plots.png", width = 1200, height = 800)  


par(mfrow = c(6, 7))  


for (loop in loop_types) {

  loop_data <- df[df$loop_type == loop, "energy_usage"]
  

  qqnorm(loop_data, main = paste("Q-Q Plot for energy usage", loop)) 
  qqline(loop_data, col = "red")  
}


dev.off()
