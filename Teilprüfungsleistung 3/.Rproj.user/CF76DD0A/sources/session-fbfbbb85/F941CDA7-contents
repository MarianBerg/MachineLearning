#Teilprüfungsleistung 3

#K4.0031_1.0_8.Ü.01
#Aufgabe Selbstorganisierende Karten – Lernrate

#Schreibe ein Programm, das die Lernrate für die Zerfallsraten lambda = 0.1, 0.5 
#und 0.99 visualisiert. Der Parameter t steht für die Anzahl der Iterationen. 
#Hierbei soll die Anzahl der Iterationen bis 60 gehen.


#lernrate_t = lernrate_0 * exp(-t*lambda) 

library(tidyverse)

n_0 <- 0.2

learning_function <- function(t, lambda) {
  
  n_0 * exp(- t * lambda)
}

data <- tibble(x = seq(0, 59))

data <- data %>%
    mutate(`lambda_0.1` = learning_function(x, 0.1),
         `lambda_0.5` = learning_function(x, 0.5),
         `lambda_0.99` = learning_function(x, 0.99)
    )

data <- data %>%
  pivot_longer(cols = starts_with("lambda"), names_to = "lambda", names_prefix = "lambda_", values_to = "y")

library(ggplot2)

ggplot(data, aes(x = x, y = y, color = lambda)) +
  geom_line() +
  labs(x = "t", y = "Lernrate",
       title = "Lernrate für verschiedene Zerfallsraten lambda")
  
         