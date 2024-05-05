class array1929 {
    public int[] getConcatenation(int[] nums) {
        int[] arr = new int[2 * nums.length];
        int temp = 0;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < nums.length; j++) {
                arr[temp] = nums[j];
                temp += 1;
            }
        }
        return arr;
    }
}