import numpy as np

#Define dataset
X = np.array(2[[2022,9.44],[2021, 9.05], [2020, 8.64],[2019, 8.19]])

#Define the number of clusters
K = 2

#Centroid random order
np.random.seed(15)
centroids = X[np.random.choice(X.shape[0], K, replace=False)]

#Assign data points to clusters
distances = np.sqrt(np.sum((X[:, np.newaxis] - centroids) **2, axis=2))
labels = np.argmin(distances, axis=1)

#Updated centroids
new_centroids = np.array([X[labels == 0].mean(axis=0), X[labels == 1].mean(axis=0)])

print("Data points:")