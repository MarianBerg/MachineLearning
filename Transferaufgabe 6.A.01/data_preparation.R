#Aufgabe: Hauspreisvorhersage mit multipler Regression
#
#In dem File HouseData.csv findest du die Hauspreise sowie Informationen zur Anzahl der Schlafzimmer, 
#Badezimmer und der Wohnfläche in Quadratfuß. Recherchiere, wie du mit sklearn die multiple Regression 
#implementieren kannst und wende sie anschließend auf die Daten an, um eine Vorhersage für die Preise 
#treffen zu können. 
#Nutze anschließend das trainierte Modell, um den Preis für ein Haus mit 3 Schlafzimmern, 2,5 Badezimmern 
#und 1.640 Quadratfuß Wohnfläche vorherzusagen (der tatsächliche Preis liegt bei 463.000 Dollar).

library(tidyverse)

data <- read_csv("HouseData.csv")

summary_stats <- data %>%
  summarise(across(where(is.numeric), list(mean = mean, sd = sd), .names = "{col}_{fn}"))

print(summary_stats)
print(summary_stats)
data_normalized <- data %>%
  mutate(price = as.vector(scale(price)),
         bedrooms = as.vector(scale(bedrooms)),
         bathrooms = as.vector(scale(bathrooms)),
         sqft_living = as.vector(scale(sqft_living))
         )

data_normalized





write_csv(data_normalized, "HouseData_normalized.csv")  
