
import matplotlib.pyplot as plt

import numpy as np
from sklearn.cluster import KMeans

X = np.array([[2,5],
             [6,4],
             [9,5],
             [8,4],
             [1,2],
             [5,9]])

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

centroid = kmeans.cluster_centers_
print("centroids are ",centroid)

plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')

plt.title("""Kmeans clustering
           black colors are centroid """)
plt.xlabel("X column data")
plt.ylabel("Y column data")

plt.show()