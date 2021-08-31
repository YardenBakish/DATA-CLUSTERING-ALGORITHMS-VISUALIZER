# 208539270 yardenbakish
# 208983700 tamircohen1
"""main program - glue to the entire project
This module calls both NSC and K-means algorithms functions and passes along
the results to the textual and visualization output files functions

The program is executed upon the invoke command named run called by setup.py file
and recieves the parameters k, n, and Random from the setup.py file"""

from sklearn.datasets import make_blobs
import numpy as np
import argparse
import random
import mykmeanssp as km
import math
import kmeans_plus as kmeans_pp
import Normalized_Spectral_Clustering as NSC
import mainPrintOutput as po



#recieving arguments from setup.py file
parser = argparse.ArgumentParser()
parser.add_argument("k", type = int)
parser.add_argument("n", type = int)
parser.add_argument("Random", type=int)
args = parser.parse_args()
k = int(args.k) # number of clusters 
n = int(args.n) # number of samples 
Random = bool(args.Random) #Random is passed as integer (0=False; 1= True)

#define constants
MAX_ITER = 300 #number of iterations for kmeans algorithm
eps = 0.0001 #constant for handling small values
max_cap=[(20,435),(20,435)] #(K,n) maximum capacity values for 2 (index=0) and 3 dimensions (index=1)
n_dim=random.randint(2,3) #choose dimension randomly
  

"""if Random is True, the value of k and n will be drawn randomly from the
range of maximum capacity and half of that value"""

if(Random):
    if(n_dim==2):
        n=random.randint(int(math.ceil(max_cap[0][1]/2)), max_cap[0][1])
        k=random.randint(int(math.ceil(max_cap[0][0]/2)), min(max_cap[0][0],n-1)) 
    else:
        n = random.randint(int(max_cap[1][1] / 2), max_cap[1][1])
        k = random.randint(int(max_cap[1][0] / 2), min(max_cap[1][0],n-1))
        
"""generating obs as the nxn matrix generated samples, and cent -The integer labels for cluster membership of each sample.
the function is called using the sklearn.datasets module and recieves n and k as paramters"""

obs,cent = make_blobs(n_samples=n, n_features=n_dim,centers=k,return_centers= False,random_state=None)


"""if k==1 at this point, it is only possible if Random=False, and k was recieved as input
in this case, simply call to the main print function (all samples in same cluster - no calculation is needed)
the main print function will now how to handle the situation (documented in the mainPrintOutput module)"""
if k==1:
    po.outputPrint(obs,cent,n_dim,None,n,1,k,None)
    exit(0)


    
"""
call for Normalized Spectral Clustering funciton from NSC module.
1. the function recieves n and k, which were drawn from the user/ randomly depandant on the Random paramter
2. the function returns spec_results, a 1d-array where the value at the i'th index is the cluster which the i'th observation was assaigned to,
   and K, the number of clusters passed along to Kmeans from NSC (could be the same k from user or caclculated
   using eigengap heuristic- depandant on Random)"""
spec_results, K = NSC.Normalized_Spectral_Clustering(obs,n,k,Random,n_dim)

"""as explained, if K==1 due to eigengap heuristic, than all samples belong to same cluster.
simply print results because no other calculation is needed"""

if K==1:
    po.outputPrint(obs,cent,n_dim,spec_results,n,1,k,None)
    exit(0)

"""calling K-means as a standalone algorithm
1. calling to kmeans_pp function which is used to choose initial centroids for K-means algorithm
2. calling to the C extension of kmeans where kmeans algorithm is executed in C. the modules recieves the initial centroids, the generated data,
   n, max iterations, the dimention of the vectors, and K - number of clusters used in kmeans called by NSC"""

#we flatten the observation matrix send it as a 1-d list
indices = kmeans_pp.kmeans_pp(obs.ravel().tolist(), K, n_dim, n)
kmeans_results= km.kmeans(K,n,n_dim,MAX_ITER, obs.ravel().tolist(), indices)


"""if kmeans returned None as its output, error occurred - print a discription of what went wrong and exit
(another massege is printed from within the kmeans C extenstion) """

if (spec_results==None or kmeans_results == None):
    print("something went wrong with kmeans")
    exit(0)


po.outputPrint(obs,cent,n_dim,spec_results,n,K,k,kmeans_results)
