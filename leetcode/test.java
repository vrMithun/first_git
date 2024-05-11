public class test {
    public String stone(int[] array) {
        int chance = 0;
        int i = 0;
        int j = i;
        int k = i;
        int bob = 0;
        int alice = 0;
        int max=0;
        while (i > array.length) {
            chance += 1;
            if(chance%2==0){
                for(;j<array.length;j++){
                    
                }
            }
        }
        System.out.println("alice=" + alice + "bob=" + bob);
        if (alice > bob) {
            return "alice";
        } else {
            return "bob";
        }
    }

    public static void main(String[] args) {
        test myobj = new test();
        int[] array = { 1, 2, 3, -9 };
        System.out.println(myobj.stone(array));
    }
}