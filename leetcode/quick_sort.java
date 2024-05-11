public class quick_sort {
    public static void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    public static void sort(int[] array, int high_index, int low_index) {
        if (low_index == high_index) {
            return;
        }
        int lp = low_index;
        int rp = high_index - 1;
        while (lp < rp) {
            while (array[lp] <= array[high_index] && lp < rp) {
                lp++;
            }
            while (array[rp] >= array[high_index] && lp < rp) {
                rp--;
            }
            swap(array, lp, rp);
        }
        swap(array, high_index, lp);
        sort(array, lp - 1, low_index);
        sort(array, high_index, lp + 1);
    }

    public static void main(String[] args) {
        int array[] = { 9, 1, 4, 3, 2 };
        sort(array, array.length - 1, 0);
        for (int i : array) {
            System.out.print(i + " ");
        }
    }
}
