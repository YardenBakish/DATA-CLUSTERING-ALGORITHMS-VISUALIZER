/*
*208539270 yardenbakish
 *208983700 tamircohen1
 * initialize.c
 *
 *  This function initializes all of the neccessary data structures in order to implement the K-means algorithm. 
 * The function's caller is the function first run by our C extension
 * The function passes along all of the data structures forward
 */



#include <stdio.h>
#include <stdlib.h>

#include "kmeans.h"

/*exec initializes all of the necessary memory structures in order to execute the algorithm
as well as converts the python objects to its equivalent C type objects
*The function returns the final result
*
* if at any point memory allocation fails, we pass along all of our pointers to a function designed to 
* free any allocated memory thus far
*/
int* exec(int* centroids, double* frame, int K, int N, int d, int I) {
	int  i = 0, j = 0, w = 0;
	
	int *c_res;
	double** observations = NULL; /*nxd matrix which contains the n points*/
	/*we need to keep track if centroids change between iterations thus we allocate two
	centroids matrices*/
	double **new_centroids = NULL;
	double** old_centroids = NULL;
	double** tmp = NULL;
	
	
	/*sizes is a helper array used to calculate the new centroid at the end of each iteration - at any point
	the i'th value is the number of observations assigned to the i'th cluster*/
	int* sizes = NULL;

	sizes = calloc(K, sizeof(int));
	if (sizes == NULL) freeArray_byFlag(frame, sizes, observations, new_centroids, old_centroids, tmp, K, 0);
	observations = calloc(N, sizeof(double *));
	if (observations == NULL) freeArray_byFlag(frame, sizes, observations, new_centroids, old_centroids, tmp, K, 0);
	new_centroids = calloc(K, sizeof(double *));
	if (new_centroids == NULL) freeArray_byFlag(frame, sizes, observations, new_centroids, old_centroids, tmp, K, 0);
	old_centroids = calloc(K, sizeof(double *));
	if (old_centroids == NULL) freeArray_byFlag(frame, sizes, observations, new_centroids, old_centroids, tmp, K, 0);

	i = 0, j = 0;
	/*as learned in class, now observation is contiguous thanks to frame variable*/
	for (i = 0; i < N; i++) {
		observations[i] = frame + i * d;
	}


	i = 0, j = 0;
	for (i = 0; i < K; i++) {
		w = centroids[i];
		
		new_centroids[i] = calloc(d, sizeof(double));
		if (new_centroids[i] == NULL) freeArray_byFlag(frame, sizes, observations, new_centroids, old_centroids, tmp, K, 0);

		old_centroids[i] = calloc(d, sizeof(double));
		if (old_centroids[i] == NULL) freeArray_byFlag(frame, sizes, observations, new_centroids, old_centroids, tmp, K, 0);
		/*we copy the coordinates of the initial observations to the cluster matrices where w is an observation*/
		for (j = 0; j < d; j++) {
			new_centroids[i][j] = observations[w][j];
			old_centroids[i][j] = observations[w][j];
		}
	}
	/*we call for iterate function upon completing the initialization of all data structures needed*/
	c_res = iterate(K, N, d, I, observations, new_centroids, old_centroids, sizes, frame);

	/*return final result*/
	return c_res;
}


