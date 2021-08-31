# 208539270 yardenbakish
# 208983700 tamircohen1
"""The Normalized Spectral Clustering Algorithm main interface
input: obs - array of n vectors with n_dim dimentions, number of clusters; and the Random parameter indicating whether the initial invoke command
of the entire program assigned True or False to Random
output: a labeling array where the value at the i'th index is the computed centroid which the i'th observation was assaigned to,
and the k used for kmeans"""

"""IMPORTANT NOTE: we dont allow division of numbers which are equal or lesser than 0.0001 as it is considered as 0 (as instructed).
in general, we treat 0.0001 as 0"""

import numpy as np
import QR_Iter as QR
import mykmeanssp as km
import kmeans_plus as kmeans_pp
import EuclideanDistance as EC
import math

#constant for kmeans' number of iterations
MAX_ITER = 300

def Normalized_Spectral_Clustering(obs,n,k, Random,n_dim):
    #Forming The Weighted Adjacency Matrix
    W = np.zeros((n, n), dtype = np.float64)
    for i in range(n):
        for j in range(i, n):
            if (i == j):
                W[i][i] = 0
            else:
                W[i][j] = np.exp(-EC.eucDist(obs[i], obs[j])/ 2) #calling euclidean distance from another module
                W[j][i] = W[i][j] #W is symmetric


    # D is the Diagonal Degree Matrix, D_half is D^-0.5
    D_half = np.zeros((n, n), dtype = np.float64)
    for i in range(n):
        sq_sum_row = np.sqrt(sum(W[i]))
        if (sq_sum_row<= 0.0001): #division by 0.0001 is considered as division by zero
            print("Divison by a value < 0.0001 while generating D^(-1/2) matrix was encountered.\nThe program will terminate")
            exit(0)
        D_half[i][i] = 1/sq_sum_row

    DWD = np.matmul(np.matmul(D_half,W, dtype = np.float64),D_half, dtype = np.float64) # D^-0.5 *W * D^-0.5

    # The Normalized Graph Laplacian
    L_norm = np.identity(n, dtype=np.float64) - DWD

    """VERY IMPORTANT NOTE: as suggested in both the project's forum and the Lecturer Messages forum,
        in order to solve the problems with dividing by zero in the modified GramSchmidt algorithm -
        we add the identity matrix to the L_norm matrix beofre calling to the QR algorithm"""

    L_norm= L_norm + np.identity(n,dtype=np.float64)

   

    
    #finding the eigenvalues and eigenvectors of L_norm

    A_bar, Q_bar = QR.QR_Iter(L_norm,n) #calling to the QR function from another module and receiving eigenvalues and eigenvectors
    # sorting eigenvalues and keeping the column's index so its possible to connect each evalue to its evector
    for i in range(n): #according to the instructions and clarifications in the project's forum - each eigenvalue smaller than 0.0001 is considered zero
        if abs(A_bar[i][i])<= 0.0001:
            A_bar[i][i] = 0
    eigenvals=sorted([(A_bar[i][i],i) for i in range (n)],key=lambda x: x[0]) #sort eigenvalues and remember their initial column index (1'th index)
    #k is either provided by user or by eigengap heuristic - depandant on Random
    if (Random == False):
        k2 = k
    else:
        #calculate k using eigengap heuristic
        eigengaps=[np.abs(eigenvals[i][0]-eigenvals[i+1][0]) for i in range(int(math.ceil(n/2)))] 
        k2=np.min(np.argmax(eigengaps))+1 # plus 1 cause 1st index is 0 (min because it returns an array)
        if k2 ==1: #if eigengap heuristic determined that k is 1 - simply return with this tuple and the rest of the algorithm will identify it (solved in main module)
            return (0,1)
   
    #step 4 of NSC algorithm 
    T = Q_bar[:,[eigenvals[i][1] for i in range(k2)]]
    #step 5 of NSC  algorithm
    for i in range(n):
        row_sum = np.sqrt(np.sum(T[i]**2))
        if row_sum <= 0.0001: #numbers below 0.0001 is considered zero - no division allowed
            print("Divison by a value < 0.0001 while generating T matrix was encountered.\nThe program will terminate")
            exit(0)
        T[i]=T[i]/row_sum

    #we flatten T and send it as a 1-d python list    
    T= T.ravel().tolist() 
    
    
    #calling for the kmeans_plus algorithm for choosing initial centroids
    indices = kmeans_pp.kmeans_pp(T,k2,k2,n)
    #calling for the kmeans algorithm implemented as C enxtension
    spec_results= km.kmeans(k2,n,k2,MAX_ITER, T, indices)
    return (spec_results,k2)
   

    
