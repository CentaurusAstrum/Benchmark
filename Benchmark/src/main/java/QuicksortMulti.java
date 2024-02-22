import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveAction;

public class QuicksortMulti extends RecursiveAction {

  private int l, r;
  private int[] numbers;

  public QuicksortMulti(int l, int r, int[] numbers) {
    this.l = l;
    this.r = r;
    this.numbers = numbers;
  }

  @Override
  protected void compute() {
    if (l < r) {
      int d = divide(l, r, numbers);
      invokeAll(new QuicksortMulti(l, d, numbers), new QuicksortMulti(d+1, r, numbers));
    }
  }

  private int divide(int l, int r, int[] numbers) {
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

  public static void sort(int[] numbers) {
    ForkJoinPool.commonPool().invoke(new QuicksortMulti(0, numbers.length-1, numbers));
  }
}
