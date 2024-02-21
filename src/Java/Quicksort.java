import java.util.Scanner;

public class Quicksort {
    
    public static void quickSort(int[] numbers, int left, int right) {
        if (left < right) {
            int piviotIndex = divide(numbers, left, right);
            quicksort(numbers, left, piviotIndex);
            quicksort(numbers, piviotIndex + 1, right);
        }
    }

    private static int divide(int[] numbers, int left, int right) {
        int pivot = numbers[left + (right - left) / 2];
        while (true) {
            while (numbers[left] < pivot) {
                left ++;
            } 
            while (numbers[right] > pivot) {
                right --;
            }
            if (left >= right) {
                return right;
            }
            int temp = numbers[left];
            numbers[left] = numbers[right];
            numbers[right] = temp;
            left ++;
            right--;

        }
    }
    
    public static void main(String[] args) {
    }
}