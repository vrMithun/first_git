public class selection_sort {
    public int[] sort(int[] array) {
        int length = array.length;
        int start = 0;
        for (int j = 0; j < length; j++) {
            int small = array[start];
            int index = start;
            for (int i = start; i < length - 1; i++) {
                if (small > array[i + 1]) {
                    small = array[i + 1];
                    index = i + 1;
                }
            }
            int temp = array[start];
            array[start] = small;
            array[index] = temp;
            start += 1;
        }
        return array;
    }

    public static void main(String[] args) {
        selection_sort myobj = new selection_sort();
        int[] array = { 9, 8, 7, 5, 2 };
        array = myobj.sort(array);
        for (int i : array) {
            System.out.print(i + " ");
        }
    }
}
