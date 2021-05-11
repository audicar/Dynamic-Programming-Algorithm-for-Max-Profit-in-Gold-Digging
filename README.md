# Dynamic-Programming-Algorithm-for-Max-Profit-in-Gold-Digging
This project utilises a dynamic programming algorithm to find the most profit achievable by a feasible mine shaft in digging.


Given as input a n x m grid represented by a 2D array A. The entry A[i][j] is an integer representing the amount of gold in cell (i, j). 

A mine shaft is represented by an n-length array S where S[i] denotes the location of the shaft at depth i. A mine shaft is feasible if it
can be realised by the robot initially drilling at S[1] and proceeding according to the following rules. 
For any depth i > 1, it can either:
1. drill straight down
2. drill down-left
3. drill down-right
It cannot drill down-right immediately after drilling down-left and it cannot drill down-left
immediately after drilling down-right
