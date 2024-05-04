public class water_trap {
    public int trap(int[] height) {
        int point, move, difference, area;
        point = 0;
        move = 1;
        int res = 0;
        while (move < height.length) {
            int result = 0;
            if ((height[point] <= height[move]) && move - point > 1) {
                difference = move - point - 1;
                area = height[point] * difference;
                result = area;
                for (int i = point + 1; i < move; i++) {
                    result = result - height[i];
                }
                point = move;
                if (move != height.length - 1) {
                    move += 1;
                } else {
                    res = res + result;
                    break;
                }
            } else if ((height[point] <= height[move]) && (move - point == 1)) {
                point = move;
                move += 1;
            } else {
                while (height[point] > height[move]) {
                    if (height.length - move != 1) {
                        move += 1;
                        break;
                    }
                    if (move == height.length - 1) {
                        if (height[move - 1] < height[move] && height[point] - height[point + 1] != 1) {
                            difference = move - point - 1;
                            area = height[move] * difference;
                            result = area;
                            for (int j = point + 1; j < move; j++) {
                                result = result - height[j];
                            }
                            move = move + 1;
                            break;
                        } else if (height[move - 1] > height[move] && height[point] - height[point + 1] != 1) {
                            move = move - 1;
                        } else {
                            point += 1;
                            move = point + 1;
                            break;
                        }

                    }
                }
            }

            res = res + result;

        }
        return res;
    }

    public static void main(String[] args) {
        water_trap myobj = new water_trap();
        int[] height = { 4, 2, 3 };
        // myobj.trap(height);
        System.out.println(myobj.trap(height));

    }
}