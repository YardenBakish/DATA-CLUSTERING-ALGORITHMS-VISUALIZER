# 208539270 yardenbakish
# 208983700 tamircohen1
"""Jaccard.py - this module calculates the Jaccard meassure for NSC and K-means"""
from math import factorial


def jaccard_similarity(a, b,k):
    a=list(a)
    b=list(b)
    #constructing lists containing the number of possible couples of samples in for each cluster.
    #the two lists are created based on the partions in lists a and b
    counts_a=[choose(a.count(i),2) for i in range(k)]
    counts_b=[choose(b.count(i),2) for i in range(k)]
    #creating a list containing a tupple with the clusters it was assigned to in each partition
    ab=[(a[i],b[i]) for i in range(len(a))]
        #for each pair of clusters from different partitions:
    # (1) The number of samples appearing in them is counted
    # (2) The number of possible pairs from the sum measured in (1) is calculated and saved
    counts_ab=[choose(ab.count((i,j)),2) for i in range(k) for j in range(k)]
    # The Jaccard meassure as defined is returned
    return sum(counts_ab)/(sum(counts_a)+sum(counts_b)-sum(counts_ab))

# This function computes the Binomial coefficient of two input numbers n and k
def choose(n,k):
    if(n>=k):
        return (factorial(n)/(factorial(k)*factorial(n-k)))
    else:
        return 0


