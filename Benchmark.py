import time, numpy as np
import multiprocessing, subprocess, os
"""
numbers = []

def numbers_generater(N):
    generated = [_ for _ in range(1, N+ 1)]
    np.random.shuffle(generated)
    numbers.extend(generated)    #Mit extend erweitere ich lediglich die Liste, mit append wäre nun eine Liste in einer Liste
    file_path = 'data/numbers.txt'
    with open(file_path, 'w') as file:
        file.write(str(numbers))
numbers_generater(1000)
"""

files = ['src/numpy_sort.py', 'src/Quicksort.py']


def run_code(file_path):
    subprocess.run(['python3', file_path], check=True)

def main(file_path):
    start_time = time.time()

    run_code(file_path)

    end_time= time.time()

    print(end_time - start_time)

if __name__ == '__main__':

    with multiprocessing.Pool(len(files)) as pool:
        pool.map(run_code, files)

