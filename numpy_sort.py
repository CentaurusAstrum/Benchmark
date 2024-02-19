import numpy as np, ast


file_path = '../data/numbers.txt'

with open(file_path, 'r') as file:
    numbers = ast.literal_eval(file.read())

sorted_numbers = np.sort(numbers)