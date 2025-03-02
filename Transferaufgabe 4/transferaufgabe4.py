
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12,4.5,5.5,9.5,3.5,11.3,13,5.01]

y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21,19.3,21.3,24.56,18.9,20.03,23,24] 



data = list(zip(x, y))

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)
print(kmeans.cluster_centers_)

plt.scatter(x, y, c = kmeans.labels_)
plt.show()