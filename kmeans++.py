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

def calc_weighting_probability(dist):

def decision_ini(data, c_num):
    dist = np.zeros(data.shape[0])
    c_ini = np.zeros((c_num, 2))
    c_ini[0] = data[np.random.randint(0, data.shape[0], 1), :, :]
    for i in range(c_num):



data  = np.loadtxt("data.csv", delimiter=",")
data_cluster = np.random.randint(0, high=3, size=data.shape[0])
