/*
*208539270 yardenbakish
 *208983700 tamircohen1
 * updateCent.c
 *
 *  
 */

#include <stdio.h>
#include <stdlib.h>
#include "kmeans.h"

/*each time we assign an observation to a cluster - we immediately calculate the NEW CURRENT
centroid location according to the observation's coordinates. the sizes array helps us
to know how many observations chose this cluster thus far  and calculate accordingly so that at the end
of an iteration we get the new centroids location properly. we change a 'new centroids' array
and keep a copy of the old ones*/


void updateCentroids(double *p1, double * p2, int size, int d) {
	int i = 0;
	for (i = 0; i < d; i++) {
		p1[i] = p1[i] + ((p2[i] - p1[i]) / size);
	}
}


