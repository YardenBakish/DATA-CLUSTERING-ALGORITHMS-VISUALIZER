/*
*208539270 yardenbakish
 *208983700 tamircohen1
 * freeAll.c
 *
 *  freeArray_byFlag - the function is designed to free all allocated memory according to the implementation of Kmeans
 *  the flag variable is incharge of freeing memory without causing errors and also to distinguish between
 * freeing memory due to error or due to successfully implementing Kmeans and leaving the program
 *
 * in order to free the memory we call the freeArray function from freeArray.c file
 *
 */


#include "kmeans.h"

void freeArray_byFlag(double *fr, int *s, double** obs, double** ncen, double** ocen, double** tmp, int i, int flag) {
	if(flag==2){
	if (tmp!= NULL) freeArray(tmp, i);}
	if (fr!=NULL) free(fr);
	if (s != NULL) free(s);
	if (obs != NULL) free(obs);
	if (ncen != NULL) freeArray(ncen, i);
	if (ocen != NULL) freeArray(ocen, i);
	if((flag==0) || (flag==2))  PyErr_SetString(PyExc_MemoryError, "Memory Allocation Error");

}
