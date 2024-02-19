"""
    The program expects a python list in a textfile as input.
    Avg. runtime of Selectionsort: O(n²)
"""

import ast

file_path = './data/numbers.txt'

with open(file_path, 'r') as file:
       numbers = ast.literal_eval(file.read())

#optimsed the alogrithmen. insted of using a tmp variable , directly switch the elements.
#this modificationen impoves runtime by up to 40%
       
def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        minIndex = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[minIndex]:
                minIndex = j
        numbers[i], numbers[minIndex] = numbers[minIndex], numbers[i]

selection_sort(numbers)