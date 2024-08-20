public class largest {
    public int findMaxK(int[] array) {
        int[] arr = new int[array.length];
        int test = 0;
        for (int i = 0; i < array.length; i++) {
            for (int j = i + 1; j < array.length; j++) {
                if (array[i] == -array[j]) {
                    if (array[i] > 0) {
                        arr[i] = array[i];
                    } else {
                        arr[i] = -array[i];
                    }
                    test += 1;
                }
            }
        }
        int greatest = arr[0];
        if (test == 0) {
            return -1;
        } else {
            for (int k = 0; k < arr.length - 1; k++) {
                if (greatest < arr[k + 1]) {
                    greatest = arr[k + 1];
                }
            }
            return greatest;
        }
    }

    public static void main(String[] args) {
        largest myobj = new largest();
        int[] array = { -37, 37, -9, 2, 47, 18, 13, -11, 9, -28 };
        System.out.println(myobj.findMaxK(array));
    }
}