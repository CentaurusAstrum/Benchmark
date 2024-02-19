import time, numpy as np
import multiprocessing, subprocess, os
import concurrent.futures
import matplotlib.pyplot as plt

numbers = []
def numbers_generater(N):
    generated = [_ for _ in range(1, N+ 1)]
    np.random.shuffle(generated)
    numbers.extend(generated)
    file_path = 'data/numbers.txt'
    with open(file_path, 'w') as file:
        file.write(str(numbers))
numbers_generater(100)


def run_code(file_path):
    local_start_time = time.time() 
    subprocess.run(['python', file_path], check=True)
    local_end_time = time.time()
    return file_path, local_end_time - local_start_time

def main():
    files = ['numpy_sort.py', 'Quicksort.py', 'Selectionsort.py', 'Bubblesort.py']
    base_path = './src/python/'
    start_time = time.time()
    result_time = []

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(run_code, base_path + file) for file in files]
        for future in concurrent.futures.as_completed(futures):
            files, execution_time = future.result()
            print(f"{files} execution time: {execution_time} seconds")
            result_time.append([files, execution_time])
    print(result_time)

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()