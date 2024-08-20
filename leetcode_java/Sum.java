import java.util.ArrayList;

class Sum {
    public int[] twoSum(int[] nums, int target) {
        ArrayList<Integer> index = new ArrayList<>();
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    index.add(i);
                    index.add(j);
                    break;
                }
            }
        }
        // Convert ArrayList to int[] array
        int[] result = new int[index.size()];
        for (int k = 0; k < index.size(); k++) {
            result[k] = index.get(k);
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;
        Sum myobj = new Sum();
        int[] result = myobj.twoSum(nums, target);
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
