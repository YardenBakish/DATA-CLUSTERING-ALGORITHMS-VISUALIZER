/*
**208539270 yardenbakish
 *208983700 tamircohen1
 * squaredEuclideanDist.c
 *
 *  
 *      
 */

#include <stdio.h>
#include <stdlib.h>
#include "kmeans.h"

/*function to calculate squared Euclidean Distance*/
double squaredEuclideanDistance(double *p1, double *p2, int d) {
	int i = 0;
	double res = 0;
	for (i = 0; i < d; ++i) {
		res += ((p1[i] - p2[i]) * (p1[i] - p2[i]));
	}
	return res;
}


