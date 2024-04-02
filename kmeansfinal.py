import numpy as np
import matplotlib.pyplot as plt

def kmeans(X,k):
    centroids = X[np.random.choice(X.shape[0],k,replace=False)]

    for _ in range(100):
        distances = np.linalg.norm(X[:,None]-centroids,axis=2)
        labels = np.argmin(distances,axis=1)
        centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
    return centroids,labels

X = np.random.rand(300,2)*10

k = 4
centroids,labels = kmeans(X,k)

plt.scatter(X[:,0], X[:,1],c=labels)
plt.scatter(centroids[:,0],centroids[:,1])
plt.title("K-Means Clustering")
plt.xlabel("Feature-1")
plt.ylabel("Feature-2")
plt.show()