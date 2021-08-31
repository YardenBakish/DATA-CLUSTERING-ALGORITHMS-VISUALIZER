/*
*208539270 yardenbakish
 *208983700 tamircohen1
 *
 * isCentroidsChanged.c
 *
 *  This C file has the centroidsChanged function - checks if any centroid shifted caused by an iteration of Kmeans
 *     
 */
#include <stdio.h>
#include <stdlib.h>
#include "kmeans.h"


/*as instructed by the forum, if the new cluster's positions is not far from 0.0001 than the original
coordinate - the centroids has not changed and we finish the kmeans algorithm. this function returns 1 is the centroids has not changed.
else it returns 0*/


int centroidsChanged(double *p1[], double *p2[], int K, int d) {
	int res = 1;
	int i = 0, j = 0;
	for (i = 0; i < K; i++) {
		for (j = 0; j < d; j++) {
			if ((p1[i][j] - p2[i][j]) > 0.0001) {
				res = 0;
				break;
			}
		}
	}
	return res;
}


