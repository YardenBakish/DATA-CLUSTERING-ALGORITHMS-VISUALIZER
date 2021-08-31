/*
 *208539270 yardenbakish
 *208983700 tamircohen1 
 *freeArray.c
 *
 *  freeArray is designed to free allocated memory from matrices
 *      
 */


#include "kmeans.h"

void freeArray(double **p, double m) {
	int i;
	for (i = 0; i < m; ++i) {
		if ((p[i])!=NULL) free(p[i]);
	}
	if (p!=NULL) free(p);
}





