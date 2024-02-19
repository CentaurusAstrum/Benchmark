"""
    The program expects a python list in a textfile as input.
    Avg. runtime of Bubblesort: O(n²)
"""

import ast

file_path = './data/numbers.txt'

with open(file_path, 'r') as file:
    numbers = ast.literal_eval(file.read())

def bubblesort(numbers):
    length = len(numbers)
    for i in range(length -1):
        swapped = False
        for j in range(length -1 -i):
            if numbers[j] > numbers[j +1]:
                numbers[j], numbers[j +1] = numbers[j +1], numbers[j]
                swapped = True
            if not swapped:
                break

bubblesort(numbers)