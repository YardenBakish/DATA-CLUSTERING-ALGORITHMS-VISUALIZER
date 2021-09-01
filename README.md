# Data-Clustering-Algorithms-Visualizer
Software Project Course - Implementation of Kmeans and Spectral Clustering algorithms in python integrated with C extensions 



**Flow**

The project will flow along these lines:
1. The user executes the program with certain arguments using the Python invoke library.
2. The program will generate random points that will be used for clustering.
3. The program will compute the clusters using two algorithms: the Normalized Spectral Clustering and K-means.
4. The program will output:

   a. A file with the resulting clusters from both algorithms.


   b. A file containing the data points that were used.


   c. A visualization file comparing the resulting clusters of the two algorithms.


**Input Arguments**

The program can be executed via the following Linux command:
```bash
python3.8.5 -m invoke run -k -n --[no-] Random
```
Where:

 • k is the number of clusters.
 
 • n is the number of data points.
 
 • Random is a Boolean typed variable with default value of True that indicates the way the data is to be generated. if Random is True,
   the   'k' and 'n' arguments has no effect on the program


