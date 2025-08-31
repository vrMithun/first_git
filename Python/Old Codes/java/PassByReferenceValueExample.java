public class PassByReferenceValueExample {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("Hello");
        modifyStringBuilder(sb);
        System.out.println("Modified value: " + sb);
    }

    public static void modifyStringBuilder(StringBuilder str) {
        str.append(" World!");
        System.out.println("Modified value inside method: " + str);
    }
}
