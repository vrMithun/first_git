import java.util.Arrays;

public class quicksort {

    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[low];
        int i = low + 1;

        for (int j = low + 1; j <= high; j++) {
            if (arr[j] < pivot) {
                swap(arr, i, j);
                i++;
            }
        }
        swap(arr, low, i - 1);
        return i - 1;
    }

    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        // Test case 1: Empty array
        int[] arr1 = {};
        quickSort(arr1, 0, arr1.length - 1);
        System.out.println(Arrays.toString(arr1)); // Expected: []

        // Test case 2: Single element
        int[] arr2 = { 5 };
        quickSort(arr2, 0, arr2.length - 1);
        System.out.println(Arrays.toString(arr2)); // Expected: [5]

        // Test case 3: Already sorted array
        int[] arr3 = { 1, 2, 3, 4, 5 };
        quickSort(arr3, 0, arr3.length - 1);
        System.out.println(Arrays.toString(arr3)); // Expected: [1, 2, 3, 4, 5]

        // Test case 4: Reverse sorted array
        int[] arr4 = { 5, 4, 3, 2, 1 };
        quickSort(arr4, 0, arr4.length - 1);
        System.out.println(Arrays.toString(arr4)); // Expected: [1, 2, 3, 4, 5]

        // Test case 5: Array with duplicates
        int[] arr5 = { 4, 2, 2, 8, 4, 1 };
        quickSort(arr5, 0, arr5.length - 1);
        System.out.println(Arrays.toString(arr5)); // Expected: [1, 2, 2, 4, 4, 8]

        // Test case 6: Array with negative numbers
        int[] arr6 = { -3, 10, -5, 2, 0 };
        quickSort(arr6, 0, arr6.length - 1);
        System.out.println(Arrays.toString(arr6)); // Expected: [-5, -3, 0, 2, 10]
    }
}