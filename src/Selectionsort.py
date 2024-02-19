"""
    The program expects a python list in a textfile as input.
    Avg. runtime of Selectionsort: O(n²)
"""

import ast

file_path = './data/numbers.txt'

with open(file_path, 'r') as file:
       numbers = ast.literal_eval(file.read())

for j in range(len(numbers)-1):
    minIndex = j
    for k in range(j+1, len(numbers)):
        if (numbers[k] < numbers[minIndex]):
                    minIndex = k
    tmp = numbers[j]
    numbers[j] = numbers[minIndex]
    numbers[minIndex] = tmp