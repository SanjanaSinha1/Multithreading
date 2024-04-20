import numpy as np
import pandas as pd
import time
import threading
import matplotlib.pyplot as plt


def generate_random_matrices(n, size):
    matrices = [np.random.rand(size, size) for _ in range(n)]
    return matrices


def multiply_matrices(constant_matrix, matrices):
    result = constant_matrix.copy()
    for matrix in matrices:
        result = np.dot(result, matrix)
    return result


def perform_multiplication_with_threads(num_threads, constant_matrix, matrices):
    start_time = time.time()
    threads = []
    matrix_batches = [matrices[i:i+num_threads] for i in range(0, len(matrices), num_threads)]

    for batch in matrix_batches:
        thread = threading.Thread(target=multiply_matrices, args=(constant_matrix, batch))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end_time = time.time()
    return end_time - start_time

# Parameters
num_matrices = 200
matrix_size = 1000
matrices = generate_random_matrices(num_matrices, matrix_size)
constant_matrix = np.random.rand(matrix_size, matrix_size)

# Perform multiplication with different numbers of threads
results = {}
for num_threads in range(1, 10):
    time_taken = perform_multiplication_with_threads(num_threads, constant_matrix, matrices)
    results[num_threads] = time_taken

# Create DataFrame
df = pd.DataFrame.from_dict(results, orient='index', columns=['Time Taken (s)'])

# Plot
df.plot(marker='o', linestyle='-')
plt.xlabel('Number of Threads')
plt.ylabel('Time Taken (s)')
plt.title('Time Taken vs Number of Threads')
plt.grid(True)
plt.show()
