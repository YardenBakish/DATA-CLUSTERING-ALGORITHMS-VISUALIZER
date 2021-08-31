# 208539270 yardenbakish
# 208983700 tamircohen1

"""This module prints the generated data and its integer label for
cluster membership of the point data ,recieved by make_blobs function,
to data.txt file"""

import numpy as np

def printData(obs,cent,n_dim):
    #creating output txt
    data_txt = open("data.txt", "w")
    for i in range(len(obs)):
        """as seen in the instrucions, we print samples up to 8 digits
        after decimal point"""
        data_txt.write(str(round(obs[i][0],8))+","+str(round(obs[i][1],8)))
        #if the dimention equals 3, print last coordinate
        if(n_dim==3):
            data_txt.write(","+str(round(obs[i][2],8)))
        data_txt.write(","+str(cent[i])+"\n")
    data_txt.close()
