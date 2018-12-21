import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = np.loadtxt("data.csv", delimiter=",")

kmeans_model = KMeans(n_clusters=3, random_state=10).fit(data)
labels = kmeans_model.labels_

for label, dat in zip(labels, data):
    print(label, dat)


for i in range(len(data)):
    if labels[i]==0:
        plt.scatter(data[i,0], data[i,1], color='r', marker='o', s=20)
    elif labels[i]==1:
        plt.scatter(data[i,0], data[i,1], color='g', marker='o', s=20)
    else:
        plt.scatter(data[i,0], data[i,1], color='b', marker='o', s=20)

plt.grid(True)
plt.show()
