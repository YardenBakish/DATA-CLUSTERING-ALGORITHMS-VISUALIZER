# 208539270 yardenbakish
# 208983700 tamircohen1
"""This module prints the computed clusters for NSC and K-means algorithms to
clusters.txt file"""
import numpy as np

"""This function is called by the main module and recieves:
(1) an array which labels each observation to its computed cluster (i'th value is the cluster for the i'th point)
(2) number of observations
(3) number of clusters.
(4) The function is called twice (for NSC and K-means) thus recieving a flag paramter
indicating the times which it was called (in order to create document or append)"""

def printClusters(label,n,K,flag):
    if (flag==0):
        clusters_txt = open("clusters.txt", "w")
        clusters_txt.write(str(K)+"\n")
    else:
       clusters_txt = open("clusters.txt", "a")
    """The function maps each cluster to its observations using python's dictionary (reverse mapping)"""
    d= {}
    for i in range(n):
        d[i] =[]
    for i in range(n):
        d[label[i]].append(i)
    """The function now prints to clusters.txt"""
    for i in range(n):
        for j in range(len(d[i])):
            if j== len(d[i])-1:
                clusters_txt.write(str(d[i][j])+"\n")
            else:
                clusters_txt.write(str(d[i][j])+",")
    clusters_txt.close()
