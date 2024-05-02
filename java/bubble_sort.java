public class bubble_sort {
    public int[] sort(int[] array1) {
        for (int i = 0; i < array1.length; i++) {
            for (int j = 0; j < array1.length - 1; j++) {
                if (array1[j] > array1[j + 1]) {
                    int temp = array1[j];
                    array1[j] = array1[j + 1];
                    array1[j + 1] = temp;
                }
            }
        }
        return array1;
    }

    public static void main(String[] args) {
        int[] array = { 3, 4, 1, 8, 3, 0 };
        bubble_sort myobj = new bubble_sort();
        myobj.sort(array);
        for (int i : array) {
            System.out.println(i);
        }
    }
}