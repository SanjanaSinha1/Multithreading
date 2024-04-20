# Multithreading
Submitted by: *Sanjana Sinha*  
Roll No: *102103040*  
Group: *3COE2*  
## Description
Multiply 200 random matrices of size 1k x 1k with a constant matrix of size 1k x 1k and generate the result table and graph. 
## Methodology:
1. Generating Random Matrices:
generate_random_matrices: Generates num_matrices random matrices of size matrix_size x matrix_size.
2. Matrix Multiplication with Threads:
multiply_matrices: Performs matrix multiplication.
perform_multiplication_with_threads: Utilizes multithreading to perform matrix multiplication with different numbers of threads.
3. Data Collection:
Collects the time taken for matrix multiplication with different numbers of threads.
4. Data Analysis:
Creates a pandas DataFrame from the collected data.
Plots the data to visualize the relationship between the number of threads and the time taken for matrix multiplication.

## Results
|Number of Threads|1|2|3|4|5|6|7|8|9|
|---|---|---|---|---|---|---|---|---|---|
|Time taken (sec)|4.637|3.941|4.203|4071|3.896|3.764|3.794|3.709|4.041|

## Graph
![multithread_table_1](https://github.com/SanjanaSinha1/Multithreading/assets/100065115/a6921ede-f944-412f-8c8e-06302dbaaef1)

## CPU
![Screenshot 2024-04-20 121220](https://github.com/SanjanaSinha1/Multithreading/assets/100065115/1fc6d9cf-c2b6-425e-9f03-98f682019a52)


The time taken is minimum when the number of threads is 8.
