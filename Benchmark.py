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
numbers_generater(10_000)

def run_code(file_path):
    local_start_time = time.time() 
    subprocess.run(['python', file_path], check=True)
    local_end_time = time.time()
    return os.path.basename(file_path), local_end_time - local_start_time

def main():
    files = ['numpy_sort.py', 'Quicksort.py', 'Selectionsort.py', 'Bubblesort.py']
    base_path = './src/python/'
    file_names = []
    execution_times = []

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(run_code, base_path + file) for file in files]
        for future in concurrent.futures.as_completed(futures):
            file_name, execution_time = future.result()
            file_names.append(file_name)
            execution_times.append(execution_time)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(file_names, execution_times, color='skyblue')
    plt.xlabel('Dateiname')
    plt.ylabel('Ausführungszeit (s)')
    plt.title('Ausführungszeit der Sortieralgorithmen')
    plt.xticks(rotation=45)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 4), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()

