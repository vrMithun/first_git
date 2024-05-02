public class insersion_sort {
    public int[] sort(int[] array) {
        for (int start = 0; start < array.length - 1; start++) {
            for (int i = start + 1; i > 0; i--) {
                if (array[i] < array[i - 1]) {
                    int temp = array[i - 1];
                    array[i - 1] = array[i];
                    array[i] = temp;
                } else {
                    break;
                }
            }
        }
        return array;
    }

    public static void main(String[] args) {
        insersion_sort myobj = new insersion_sort();
        int[] array = { 9, 4, 2, 1, 3 };
        array = myobj.sort(array);
        for (int i : array) {
            System.out.print(i + " ");
        }
    }
}