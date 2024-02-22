import java.util.Arrays;

public class Quicksort {

  private int l, r;
  private int[] numbers;

  public static void sort(int[] numbers) {
    quicksort(0, numbers.length-1, numbers);
  }

  public static int divide(int l, int r, int[] numbers) {
    int p = numbers[(l + r) / 2];
      while (true) {
        while (numbers[l] < p)
          l++;
        while (numbers[r] > p)
          r--;
        if (l < r) {
          int tmp = numbers[l];
          numbers[l] = numbers[r];
          numbers[r] = tmp;
        } else
          return r;
      }
  }

  public static void quicksort(int l, int r, int[] numbers) {
    if (l < r) {
      int d = divide(l, r, numbers);
      quicksort(l, d, numbers);
      quicksort(d+1, r, numbers);
    }
  }
}
