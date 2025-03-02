library(tidyverse)


data <- read_csv("Gehaltsklassen.csv")

data <- as_tibble(data)

summary(data)


data <- data %>% 
  rename(gehalt_over_50k = `Gehalt >50k`)

data <- data %>%
  mutate(
    Bildungsgrad = fct_relevel(Bildungsgrad, "Ausbildung", "Abitur", "Bachelor", "Master", "PhD"),
    gehalt_over_50k = fct_relevel(gehalt_over_50k , "nein", "ja")
  )

data_final <- data %>% 
  mutate(
    Bildungsgrad = as.numeric(Bildungsgrad),
    gehalt_over_50k = as.numeric(gehalt_over_50k)
  )

write_csv(data_final, "Gehaltsklassen_prepared.csv")


