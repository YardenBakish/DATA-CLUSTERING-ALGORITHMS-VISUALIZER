/*208539270 yardenbakish
 *208983700 tamircohen1
 * kmeans.h
 *
 *  main header file for all functions that are part of kmeans algorithm
 *  a SHORT BRIEF is given here for each function - FURTHER DETAILS are in the other c files     
 */
#define PY_SSIZE_T_CLEAN
#include <Python.h>


int centroidsChanged(double *p1[], double *p2[], int, int); /*used to check whether two arrays dont differ from one another by more than 0.0001*/
void updateCentroids(double *p1, double * p2, int size, int d); /*in the kmeans iterations - upon each assaignment of observation to cluster - we update cluster's coordinates accordingly*/
double squaredEuclideanDistance(double *p1, double *p2, int d); /*helper function to calculate euclidean distance*/
void freeArray(double **p, double m); /*helper function to free pointer's array properly*/
void freeArray_byFlag(double *fr, int *s, double** obs, double** ncen, double** ocen, double** tmp, int i, int flag); /*proper explaination in the freaAll.c file*/
int* exec(int* centroids, double* frame, int K, int N, int d, int I); /*deals with memory allocation of different data structures used for the kmeans iterations*/
int* iterate(int K, int N, int d, int I, double** obs, double** nCen, double** oCen, int* sizes, double* frame); /*computes kmeans and returns an array where the value of the i'th cell is 
																												 the cluster assained to the i'th point*/




