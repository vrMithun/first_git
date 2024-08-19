class Solution {
    public String reversePrefix(String word, char ch) {
        String word3, word2 = "";
        int t = 0;
        StringBuilder sb = new StringBuilder(word);
        int i;
        for (i = 0; i < sb.length(); i++) {
            char letter = sb.charAt(i);
            if (letter == ch) {
                word3 = sb.delete(i + 1, sb.length()).toString();
                System.out.println(word3);
                StringBuilder tempBuild = new StringBuilder(word3);
                word2 = tempBuild.reverse().toString();
                System.out.println(word2);
                t = t + 1;
                break;
            }
        }
        if (t == 1) {
            StringBuilder w = new StringBuilder(word);
            return w.replace(0, i + 1, word2).toString();
        } else {
            return word;
        }
    }

    public static void main(String[] args) {
        Solution myobj = new Solution();
        System.out.println(myobj.reversePrefix("abcdefd", 'd'));
    }
}