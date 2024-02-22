import java.util.*;

public class Main {
  public static void main(String[] args) {
    int size = 50_000_000;
    if(args.length > 0) {
      size = Integer.parseInt(args[0]);
    }
    int[] numbers = generateNumbers(size);
    float resultTime1 = runBenchmarkSingleThread(numbers);
    float resultTime2 = runBenchmarkMultiThread(numbers);

    System.out.printf(Locale.ENGLISH, "Quicksort with %,d elements%n" +
        "Sorting time: %.3f seconds (single)%n" +
        "Sorting time: %.3f seconds (multi)%n",
        size, resultTime1, resultTime2);
  }

  public static float runBenchmarkSingleThread(int[] numbers) {
    long startTime = System.currentTimeMillis();
    Quicksort.sort(numbers);
    long endTime = System.currentTimeMillis();
    // Convert to seconds by dividing with 1000
    return (endTime - startTime) / 1000f;
  }

  public static float runBenchmarkMultiThread(int[] numbers) {
    long startTime = System.currentTimeMillis();
    QuicksortMulti.sort(numbers);
    long endTime = System.currentTimeMillis();
    // Convert to seconds by dividing with 1000
    return (endTime - startTime) / 1000f;
  }

  public static int[] generateNumbers(int size) {
    int[] array = new int[size];

    // Fill the array with numbers from 1 to n
    for (int i = 0; i < size; i++) {
      array[i] = i + 1;
    }

    // Shuffle the array
    Random rand = new Random();
    for (int i = 0; i < size; i++) {
      int randomIndexToSwap = rand.nextInt(size);
      int temp = array[randomIndexToSwap];
      array[randomIndexToSwap] = array[i];
      array[i] = temp;
    }

    return array;
  }
}
