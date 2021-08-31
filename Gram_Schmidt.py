# 208539270 yardenbakish
# 208983700 tamircohen1
"""Gram_Schmidt - decomposes a nxn matrix into product QR of and orthogonal matrix Q
and an upper triangular matrix R. The module is called by the QR algorithm."""

"""NOTE 1 (IMPORTANT): as suggested in the project's forum, we followed the exact suggestion brought up-
we added the identity matrix to the L_norm matrix before calling for the QR algorithm (executed in the Normalized_Spectral_Clustering module.
if R[i][i] <= 0.0001, we treat the division outcome as 0 and continue"""

"""NOTE 2 (IMPORTANT): Q and R matrices used in this alogirthm were initialized in the QR algorithm (different module) and are
passed as parameters- no need to initialize each time we call mgs"""

"""NOTE3: each line in the function has a note next to it specifying the corresponding line in the
provided psuedo-code"""


import numpy as np
import EuclideanDistance as EC

def Gram_Schmidt(A,n,R,Q):
    U=A #line 1
    for i in range(n): #line 2
        U_i = U[:,i] #line 3
        R[i][i]=EC.eucDist(U_i, np.zeros(n, dtype = np.float64)) #line 3
        if (R[i][i] <=0.0001): #if R[i][i] <=0.0001 the outcome of division is treated as zero. else, we do what is expected
            Q[:,i]=0
        else:
            Q[:,i]=U_i/R[i][i] #line 4
        Q_i = Q[:,i].T #line 6
        R[i,i+1:n]= np.matmul(Q_i,U[:,i+1:n], dtype = np.float64) #line 5 - we use slicing - no need for inner loop (same action)
        U[:, i+1:n] -= np.matmul(Q[np.newaxis,:,i].T,R[np.newaxis,i, i+1:n], dtype = np.float64) #line 7 -  we use slicing - no need for inner loop (same action) 

    return Q,R
