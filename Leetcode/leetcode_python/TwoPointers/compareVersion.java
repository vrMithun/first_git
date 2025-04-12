import java.util.ArrayList;

class Solution {
    public int compareVersion(String version1, String version2) {
        char[] chararr1 = version1.toCharArray();
        char[] chararr2 = version2.toCharArray();
        StringBuilder sb = new StringBuilder("");
        ArrayList<Integer> arr1 = new ArrayList<Integer>();
        ArrayList<Integer> arr2 = new ArrayList<Integer>();
        int t = 0;
        for (char s : chararr1) {
            if (s != '.') {
                sb.append(s);
            } else {
                String str = sb.toString();
                int value = Integer.parseInt(str);
                arr1.add(value);
                sb.setLength(0);  
            }
        }
        if (sb.length() > 0) {
            int value = Integer.parseInt(sb.toString());
            arr1.add(value);
            sb.setLength(0);
        }
        for (char s : chararr2) {
            if (s != '.') {
                sb.append(s);
            } else {
                String str = sb.toString();
                int value = Integer.parseInt(str);
            
                arr2.add(value);
                sb.setLength(0);
                
            }
        }
        if (sb.length() > 0) {
            int value = Integer.parseInt(sb.toString());
            arr2.add(value);
        }
        int j=0;
        int minLength = Math.min(arr1.size(), arr2.size());
        if (arr1.size() != arr2.size()) {
            for(; j<minLength;j++){
                if(arr1.get(j)>arr2.get(j)){
                    t=1;
                    break;
                }
                else if (arr1.get(j) < arr2.get(j)){
                    t=-1;
                    break;
                }
            }
            int diff;
            if(arr1.size()>arr2.size() && t==0){
                diff=arr1.size()-arr2.size();
                for(int l=j;l<j+diff;l++){
                    if(arr1.get(l)!=0){
                        t=1;
                        break;
                    }
                }
            }
            else if(arr1.size()<arr2.size() && t==0){
                diff=arr2.size()-arr1.size();
                for(int k=j;k<j+diff;k++){
                    if(arr2.get(k)!=0){
                        t=-1;
                        break;
                    }
                }
            }
        } else {
            if (arr1.equals(arr2)) {
                t = 0;
            } else {
                for (int i = 0; i < arr1.size(); i++) {
                    int temp = arr1.get(i) - arr2.get(i);
                    System.out.println(temp);
                    if (temp > 0) {
                        t = 1;
                        break;
                    } else if (temp < 0) {
                        t = -1;
                        break;
                    }
                }
            }

        }
        return t;
    }

    public static void main(String[] args) {
        Solution myobj = new Solution();
        String version1 = "10.20";
        String version2 = "10.21";
        System.out.println(myobj.compareVersion(version1, version2));
    }
}