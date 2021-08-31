# 208539270 yardenbakish
# 208983700 tamircohen1
"""This module oversees the graphic output of our project in our clusters.pdf file,
containing the information on the calculated clusters"""

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import Jaccard


def visualize(spec_res,kmeans_res,obs,cent,K,k,n_dim):
    
    n=len(obs)
    #calculate Jaccard measures using Jaccard module
    
    Jaccard_spectral = Jaccard.jaccard_similarity(spec_res, cent,K)
    
    Jaccard_kmeans = Jaccard.jaccard_similarity(kmeans_res, cent,K)
    
    # list of K colors, each assigned to a different cluster in the plots
    colors=cm.rainbow(np.linspace(0, 1,K))
    fig = plt.figure(figsize=(8.27, 6))
    # producing the text containing the relevant information about the results
    txt = "Data was generated from the values:\n"+"n = "+str(n)+" , k = "+str(k)+"\nThe k that was used for both" \
                " algorithms was " + str(K)+"\nThe Jaccard measure for Spectral Clustering: " + str(round(Jaccard_spectral, 2))+\
               "\nThe Jaccard measure for K-means: " + str(round(Jaccard_kmeans, 2))
    
    if(n_dim==2):
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
        plt.gcf().subplots_adjust(bottom=0.3)
        # inserting samples into the Normalized Spectral Clustering plot
        for i in range(len(spec_res)):
            ax1.plot(obs[i][0],obs[i][1],'o',c=colors[spec_res[i]],alpha=1)
        # inserting samples into the K-means plot
        for i in range(len(kmeans_res)):
            ax2.plot(obs[i][0], obs[i][1], 'o', c=colors[kmeans_res[i]],alpha=1)
        plt.figtext(0.5, 0.1,txt, ha="center", fontsize=10)
    else:
        ax1 = fig.add_subplot(121, projection='3d')
        ax2 = fig.add_subplot(122, projection='3d')
        plt.gcf().subplots_adjust(top=1.2)
        # inserting samples into the Normalized Spectral Clustering plot
        for i in range(len(spec_res)):
            ax1.plot(obs[i][0], obs[i][1],obs[i][2], 'o',markersize=4, c=colors[spec_res[i]],alpha=1)
        # inserting samples into the K-means plot
        for i in range(len(kmeans_res)):
            ax2.plot(obs[i][0], obs[i][1],obs[i][2], 'o',markersize=4, c=colors[kmeans_res[i]],alpha=1)
        plt.figtext(0.5, 0.2,txt, ha="center", fontsize=10)
    
    ax1.grid(True)
    ax1.set_title('Normalized Spectral Clustering')
    ax2.grid(True)
    ax2.set_title('K-means')
    plt.savefig("clusters.pdf") #saving the pdf file
    plt.close()
