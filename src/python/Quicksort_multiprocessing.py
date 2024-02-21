import multiprocessing
import ast

def quicksort(numbers):
    def divide(numbers, l, r):
        pivot = numbers[l + (r - l) // 2]
        while True:
            while numbers[l] < pivot:
                l += 1
            while numbers[r] > pivot:
                r -= 1
            if l >= r:
                return r
            numbers[l], numbers[r] = numbers[r], numbers[l]
            l += 1
            r -= 1

    def quicksort_helper(numbers, l, r):
        if l < r:
            pivotIndex = divide(numbers, l, r)
            quicksort_helper(numbers, l, pivotIndex)
            quicksort_helper(numbers, pivotIndex + 1, r)

    quicksort_helper(numbers, 0, len(numbers) - 1)
    return numbers

def sort_sublist(numbers, queue):
    sorted_list = quicksort(numbers)
    queue.put(sorted_list)

def main():
    file_path = '../../data/numbers.txt'
    with open(file_path, 'r') as file:
        numbers = ast.literal_eval(file.read())

    # Teile die Liste in zwei Hälften
    mid_point = len(numbers) // 2
    first_half = numbers[:mid_point]
    second_half = numbers[mid_point:]

    # Erstelle eine Queue, um die sortierten Listen zu sammeln
    queue = multiprocessing.Queue()

    # Erstelle und starte die Prozesse
    p1 = multiprocessing.Process(target=sort_sublist, args=(first_half, queue))
    p2 = multiprocessing.Process(target=sort_sublist, args=(second_half, queue))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    sorted_first_half = queue.get()
    sorted_second_half = queue.get()

    # Die Listen müssten dann zusammengeführt werden, falls erforderlich
    # Dieser Schritt wird hier nicht gezeigt

if __name__ == '__main__':
    main()
