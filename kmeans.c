/*
 *208539270 yardenbakish
 *208983700 tamircohen1
 *
 *kmeans.c - This extension is used in order to implement the K-means algorithm. This extension is called
 *twice - as part of the Normalized Spectral Clustering algorithm and as a standalone algorithm
 *
 *this extension eventually returns a label array where the value at the i'th value is the cluster
 *in which the i'th point was assigned to.
 */

/*
NOTE: all of our c files are designed in a way such that if an error occurs - we free all of the current allocated memory,
print a description of what happened, and exit
*/

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

#include "kmeans.h"







/*The starting Function - this function is called first in this C extension of Kmeans 
* input: k,n, number of iterations (300), points' dimension (2 or 3), the observations as a flattened python list, and 
* the initial centroids chosen. 
*
*NOTE: for every memoryError/ Runtime Error we print a description of what happened, free allocated memory, and exit the program
* in each C File
*/
static PyObject* kmeans_alg(PyObject *self, PyObject *args) {
	PyObject* _observations;
	PyObject* _centroids;
	PyObject *item;
	PyObject *cluster;
	PyObject* result;
	int MAX_ITER, K, N, d, w;
	int i = 0;
	double* frame = NULL;
	int* centroids = NULL;
	int* c_res;


	/*pass along the arguments and convert them to C/pyObject objects*/
	if (!PyArg_ParseTuple(args, "iiiiOO", &K, &N, &d, &MAX_ITER, &_observations, &_centroids)) {
		PyErr_SetString(PyExc_RuntimeError, "arguments were not received properly from python");
	}

	if (!PyList_Check(_observations) || !PyList_Check(_centroids)) {
		PyErr_SetString(PyExc_RuntimeError, "observations and/or initial centroids are not of type list - terminate");
	}
	/*allocate memory and convert observations and initial clusters array from python-types*/
	centroids  = calloc(K, sizeof(int));
	if (centroids == NULL) PyErr_SetString(PyExc_MemoryError, "Memory Allocation Error");
	frame = calloc(N*d, sizeof(double));
	if (frame == NULL) {
		free(centroids);
		PyErr_SetString(PyExc_MemoryError, "Memory Allocation Error");
	}

	for (i = 0; i < K; i++) {
		item = PyList_GetItem(_centroids, i); /*extract values from the centroid array*/
		if (!PyLong_Check(item)) continue;
		w = (int)PyLong_AsLong(item); /*w is the initial observation assigned to current i'th cluster*/
		centroids[i] = w;
	}

	for (i = 0; i < N*d; i++) {
		item = PyList_GetItem(_observations, i); /*convert value at i'th index in the _obs python list to C-type*/
		if (!PyFloat_Check(item)) continue; /*assert that observation coordinate if of type float*/
		frame[i] = PyFloat_AsDouble(item);
	}

	/*we call for exec function*/
	result = PyList_New(N);
	c_res = exec(centroids, frame, K, N, d, MAX_ITER);
	/*result array received - convert it to python and return*/
	for (i = 0 ;i < N; i++) {
		cluster = Py_BuildValue("i", c_res[i]);
		PyList_SetItem(result, i, cluster);
	}
	
	
	free(c_res);
	free(centroids);
	/*return final result*/

	return result;
}





/*RELEVANT TO TRANSFER INFORMATION BETWEEN PYTHON AND C EXTENSION*/

static PyMethodDef capiMethods[] = {
    {"kmeans",                   /* the Python method name that will be used */
      (PyCFunction) kmeans_alg, /* the C-function that implements the Python function and returns static PyObject*  */
      METH_VARARGS,           /* flags indicating parameters
accepted for this function */
      PyDoc_STR(" ")}, /*  The docstring for the function */
    {NULL, NULL, 0, NULL}     /* The last entry must be all NULL as shown to act as a
                                 sentinel. Python looks for this entry to know that all
                                 of the functions for the module have been defined. */
};

static struct PyModuleDef _moduledef = {
    PyModuleDef_HEAD_INIT,
    "mykmeanssp", /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,  /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    capiMethods /* the PyMethodDef array from before containing the methods of the extension */
};
/*return the module to python*/
PyMODINIT_FUNC
PyInit_mykmeanssp(void)
{
    PyObject *m;
    m = PyModule_Create(&_moduledef); // CREATING OUR MODEL
    if (!m) {
        return NULL;
    }
    return m;
}








