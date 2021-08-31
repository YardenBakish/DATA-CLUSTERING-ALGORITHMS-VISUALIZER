# 208539270 yardenbakish
# 208983700 tamircohen1
"""Helper functions for calculating Euclidean Distance (Squared or not)
the functions are called when creating the weighted matrix and choosing inital clusters
for the K-means algorithm"""
import numpy as np

#Euclidean Distance
def eucDist(x, y):
    S  =np.sqrt(np.sum((x-y)**2))
    return S

#Squared Euclidean Distance 
def sqEucDist(x, y):
    S = 0
    for i in range(len(x)):
        S += (pow(float(x[i])-float(y[i]), 2))
    return S
