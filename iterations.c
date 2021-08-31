/*
* 208539270 yardenbakish
 *208983700 tamircohen1
 *
 * iterations.c
 *
 *  iterations function - our main function where we run the Kmeans iterations upon reciving the initialized data structures
 *      
 */


#include <stdio.h>
#include <stdlib.h>

#include "kmeans.h"


/*iterate is our main function where the iterations of Kmeans occur. the function returns the final output, and returns it to the exec function*/

int* iterate(int K, int N, int d, int I, double** obs, double** nCen, double** oCen, int* sizes, double* frame) {
	int i = 0, j = 0, bool = 0, iteration = 0, size = 0;
	double minimum = 0;
	double** tmp = NULL;
	int* c_res = NULL;
	 /*create python list in size n*/
	while (iteration < I) { /*loop in number of I*/
		for (i = 0; i < N; i++) { /*for every observation*/
			int min_cen = 0;
			/*calculate nearest centroid to observation by calling to an euclidean distance function (built in another C file)*/
			minimum = squaredEuclideanDistance(obs[i], oCen[0], d);
			for (j = 1; j < K; ++j) {
				double x = squaredEuclideanDistance(obs[i], oCen[j], d);
				if (x < minimum) {
					minimum = x;
					min_cen = j;
				}
			}
			/*add 1 to sizes in the min_cen cell indicating there is another observation assigned
			to this cluster thus far in this iteration*/
			sizes[min_cen] += 1;
			size = sizes[min_cen]; /*get how many observations are in this cluster currently*/
			/*update new centroid location according to how many observations has been assigned and observation's coordinates (external C file)*/
			updateCentroids(nCen[min_cen], obs[i], size, d);
		}
		/*check if centroids shifted by more than 0.0001 from their original location*/
		bool = centroidsChanged(nCen, oCen, K, d);
		/*if bool==1 (centroids not changed) or if we are on our last iteration*/
		if ((bool == 1) || (iteration == I - 1)) {
			/*compute last coordinates of centroids and assign observations to them*/
			c_res = calloc(N, sizeof(int));
			if (c_res == NULL) {
				free(c_res);
				freeArray_byFlag(frame, sizes, obs, nCen, oCen, tmp, K, 0);
			}
			for (i = 0; i < N; i++) {
				int min_cen = 0;
				minimum = squaredEuclideanDistance(obs[i], oCen[0], d);
				for (j = 1; j < K; ++j) {
					double x = squaredEuclideanDistance(obs[i], oCen[j], d);
					if (x < minimum) {
						minimum = x;
						min_cen = j;
					}
					/*we finished checking who is the computed cluster for the i'th observation - write
					in the i'th cell the number of cluster which is nearest to the observation - thus computing the centroid
					that matches the observation*/
					if (j == K - 1) {
						c_res[i] = min_cen;
					}
				}
			}
			/*break main loop*/
			break;
		}
		/*if we are here there are still more iteration to go*/
		/*initialize the new centroids locations; take the old centroids and make them the new centroids which
		were computed this iteration (used to check if centroids changed from last iteration*/
		tmp = calloc(K, sizeof(double *));
		if (tmp == NULL) {
			freeArray_byFlag(frame, sizes, obs, nCen, oCen, tmp, K, 2); /*allocation failed - free all allocated memory in program*/
		}
		i = 0;
		for (i = 0; i < K; i++) {
			tmp[i] = calloc(d, sizeof(double));
			if (tmp[i] == NULL) {
				freeArray_byFlag(frame, sizes, obs, nCen, oCen, tmp, K, 2);
			}
		}
		/*no use for the old centroids - free them*/
		freeArray(oCen, K);
		oCen = NULL;
		oCen = nCen;
		nCen = tmp;
		i = 0;
		/*initialize the sizes array - no observation assigned to no cluster*/
		for (i = 0; i < K; i++) {
			sizes[i] = 0;
		}
		/*next iteration*/
		iteration += 1;
	}
	/*free all memory and return result*/
	freeArray_byFlag(frame, sizes, obs, nCen, oCen, tmp, K, 1);

	return c_res;
}






