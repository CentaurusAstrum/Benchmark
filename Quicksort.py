"""
    The program expects a python list in a textfile as input.
    Avg. runtime of Quickssort: O(n*log(n))
"""

import ast

file_path = '../data/numbers.txt'

with open(file_path, 'r') as file:
     numbers = ast.literal_eval(file.read())

def quicksort(l, r):
        if (l < r):
            d = divide(l, r)
            quicksort(l, d)
            quicksort(d+1, r)

def divide(l, r):
    p = numbers[int((l + r) / 2)]
    while (1):
        while (numbers[l] < p):
            l = l+1
        while (numbers[r] > p):
            r = r-1
        if (l < r):
            tmp = numbers[l]
            numbers[l] = numbers[r]
            numbers[r] = tmp
        else:
            return r
        
quicksort(0, len(numbers) -1)