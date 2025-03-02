
import pandas as pd

data = pd.read_csv("HouseData.csv")

features = data[['bedrooms', 'bathrooms', 'sqft_living']]
labels = data['price']

from sklearn import linear_model
my_model = linear_model.LinearRegression()
my_model.fit(features, labels)
prediction = my_model.predict([[3, 2.5, 1640]])

print("\n")
print("Der Vorhergesagte Wert betraegt: {} Dollar".format(prediction))


data_normalized = pd.read_csv("HouseData_normalized.csv")

features = data_normalized[['bedrooms', 'bathrooms', 'sqft_living']]
labels = data_normalized['price']
#price_mean price_sd bedrooms_mean bedrooms_sd bathrooms_mean bathrooms_sd sqft_living_mean sqft_living_sd
#       <dbl>    <dbl>         <dbl>       <dbl>          <dbl>        <dbl>            <dbl>          <dbl>
#1    458878.  195814.          3.33       0.845           2.01        0.730            2057.           886.
from sklearn import linear_model
my_model = linear_model.LinearRegression()
my_model.fit(features, labels)
prediction = my_model.predict([[(3 - 3.33)/0.845 , (2.5 - 2.01)/0.730, (1640 - 2057)/886]])

print("\n")
print("Der Vorhergesagte Wert betraegt: {} Dollar".format((prediction * 195814) + 458878))