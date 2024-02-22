import java.util.*;

public class Main {
  public static void main(String[] args) {
    System.out.println("### Quicksort ###");
    int[] numbers = generateNumbers(20_000_000);
    float resultTime1 = runBenchmarkSingleThread(numbers);
    System.out.printf(Locale.ENGLISH, "Sorting time: %.3f seconds (single)", resultTime1);
    //TODO
//    float resultTime2 = runBenchmarkMultiThread(numbers);
//    System.out.printf(Locale.ENGLISH, "Sorting time: %.3f seconds (multi)", resultTime2);
  }

  public static float runBenchmarkSingleThread(int[] numbers) {
    long startTime = System.currentTimeMillis();
    Quicksort quicksort = new Quicksort();
    quicksort.sort(numbers);
    long endTime = System.currentTimeMillis();
    // Convert to seconds by dividing with 1000
    return (endTime - startTime) / 1000f;
  }

//  public static float runBenchmarkMultiThread(int[] numbers) {
//    long startTime = System.currentTimeMillis();
//    QuicksortMulti quicksort = new QuicksortMulti();
//    quicksort.sort(numbers);
//    long endTime = System.currentTimeMillis();
//    // Convert to seconds by dividing with 1000
//    return (endTime - startTime) / 1000f;
//  }

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
