import numpy as np
import matplotlib.pyplot as plt

def distance(a, b):
    dist = 0.0
    for i in range(len(a)):
        dist = (a[i] - b[i])**2
    dist = np.sqrt(dist)
    return dist

def get_center(data, c_num):
    c_x = 0
    c_y = 0
    count = 0.0000001
    for i in range(data.shape[0]):
        if data_cluster[i] == c_num:
            c_x += data[i, 0]
            c_y += data[i, 1]
            count += 1
    c_x /= count
    c_y /= count

    return c_x, c_y

data  = np.loadtxt("data.csv", delimiter=",")
data_cluster = np.random.randint(0, high=3, size=data.shape[0])
cluster_center = np.zeros((3, 2))
dist = np.zeros(3)

cluster_center[0] = get_center(data, 0)
cluster_center[1] = get_center(data, 1)
cluster_center[2] = get_center(data, 2)

for time in range(10):
    for i in range(data.shape[0]):
        dist[0] = distance(data[i], cluster_center[0])
        dist[1] = distance(data[i], cluster_center[1])
        dist[2] = distance(data[i], cluster_center[2])
        data_cluster[i] = np.argmin(dist)

    cluster_center[0] = get_center(data, 0)
    cluster_center[1] = get_center(data, 1)
    cluster_center[2] = get_center(data, 2)


for i in range(len(data)):
    if data_cluster[i]==0:
        plt.scatter(data[i,0], data[i,1], color="r", marker="o", s=20)
    elif data_cluster[i]==1:
        plt.scatter(data[i,0], data[i,1], color="g", marker="o", s=20)
    else:
        plt.scatter(data[i,0], data[i,1], color="b", marker="o", s=20)

plt.grid(True)
plt.show()
