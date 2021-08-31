# 208539270 yardenbakish
# 208983700 tamircohen1
"""This module is the glue for all output functions"""


import dataOutput as da
import clustersOutput as cs
import Visualize as vis


"""calling to all textual and visualization output functions using the generated data and computed clusters"""
"""the computed clusters are recieved as a label array (spec_results and kmeans_results) for both algorithms
where the value at the i'th index is the cluster which the i'th pointed was labeled to"""
def outputPrint(obs,cent,n_dim,spec_results,n,K,k,kmeans_results):
    if K==1: #if K==1 all n points are labeled to same cluster (nevermind which cluster)
        kmeans_results = [0 for i in range(n)]
        spec_results = [0 for i in range(n)]
    
    da.printData(obs,cent,n_dim)
    cs.printClusters(spec_results,n,K,0)
    cs.printClusters(kmeans_results,n,K,1)
    vis.visualize(spec_results,kmeans_results,obs,cent,K,k,n_dim)
