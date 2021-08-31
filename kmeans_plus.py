# 208539270 yardenbakish
# 208983700 tamircohen1
"""kmeans_plus - This module chooses initial k clusters out of n observations
and returns an array where the value in the i'th cell is the observation choosen
for the i'th centroid. the function is called from the NSC and main modules"""


import EuclideanDistance as EC
import numpy as np

def kmeans_pp(observations, K, D, N):
    np.random.seed(0)  # Seed randomness
    selected_indices = [] #indices of observations selected as centroids
    indices = np.arange(0, N)  #indices of all centroids

    #selecting first centroid at random
    index = np.random.choice(indices)
    selected_indices.append(int(index))
    D_list = np.zeros(N) # list of minimal squared euclidean distance for each observation

    # computing the squared euclidean distance from the selected first centroid to all observations
    for i in range(N):
        # calculating squared euclidean distance (using a different module)
        D_list[i]=EC.sqEucDist(observations[i*D:(i+1)*D],observations[index*D:(index+1)*D])

    # selecting the k-1 remaining centroids
    for j in range(2, K+1):
        # for each observation calculate D_i
        for i in range (N):
            t=selected_indices[-1]
            """calculating squared euclidean distance (using a different module) and keeping the minimum between the
             value from the previous iteration and the value calculated in the current one."""
            #calculating squared euclidean distance (using another module)
            D_list[i]=np.minimum(EC.sqEucDist(observations[i*D:(i+1)*D],observations[t*D:(t+1)*D]),D_list[i]) 
        prob=D_list/np.sum(D_list) # computing the probability of selecting each observation for the j'th cluster

        """selecting the j'th cluster inital observations' index from the remaining observations using the probability 
        density function defined in the previous line"""
        index=np.random.choice(indices,p=prob)
        selected_indices.append(int(index))

    return selected_indices
