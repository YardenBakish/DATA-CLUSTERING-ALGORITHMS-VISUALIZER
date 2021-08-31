# 208539270 yardenbakish
# 208983700 tamircohen1
"""QR_Iter - outputs an orthogonal matrix Q_bar whose columns approach the eigen
vectors of A and matrix A_bar whose diagonal elements approach the eigenvalues of
A. each column i, corresponds to the i'th eigenvector"""

"""NOTE1: Q and R matrices are already initialized in this function - no need to initialize
every time we call GramSchmidt"""

"""NOTE2: each line in the function has a note next to it specifying the corresponding line in the
provided psuedo-code"""

"""NOTE3: the QR_Iter function is called from the Normalized_Spectral_Clustering - where it is detailed
that we added the identity matrix to the L_norm matrix which is recieved as argument (as suggested in project's forum)"""


import Gram_Schmidt as GS
import numpy as np


eps = 0.0001

def QR_Iter(A,n):
    A_bar= A #line 1 
    Q_bar=np.identity(n, dtype = np.float64) #line 2
    R=np.zeros((n,n), dtype = np.float64) #initialize matrices for Gram_Schmidt
    Q = np.zeros((n,n), dtype = np.float64)
    for i in range(n): #line 3
        Q,R= GS.Gram_Schmidt(A_bar,n,R,Q) #line 4 - calling Gram-Schmidt algorithm for product decomposition
        A_bar=np.matmul(R,Q, dtype = np.float64) #line 5
        Q_bar_Q= np.matmul(Q_bar,Q, dtype = np.float64) #line 6
        if(np.all(np.abs(np.abs(Q_bar)-np.abs(Q_bar_Q))<=eps)):
            return A_bar,Q_bar #line 7
        Q_bar=Q_bar_Q #line 9
    return A_bar, Q_bar #line 11
