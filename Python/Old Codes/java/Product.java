import java.util.Scanner;

public class Product {
    public int Pid;
    public String Pname;
    public int Cost;
    private double Discount;
    private double Final_Price;
    public String Product_type;
    private double Profit;

    public void Set_Data() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter Product ID:");
        Pid = scanner.nextInt();
        scanner.nextLine();
        System.out.println("Enter Product Name:");
        Pname = scanner.nextLine();
        System.out.println("Enter Product Cost:");
        Cost = scanner.nextInt();
        scanner.close();

        Discount = 0.20; // 20%
        Final_Price = Cost - (Cost * Discount);
        Product_type = "Mobile";

        calculate_profit();
    }

    public void Print_Data() {
        System.out.println("Product ID: " + Pid);
        System.out.println("Product Name: " + Pname);
        System.out.println("Product Cost: " + Cost);
        System.out.println("Discount: " + (Discount * 100) + "%");
        System.out.println("Final Price: " + Final_Price);
        System.out.println("Product Type: " + Product_type);
        System.out.println("Profit: " + Profit);
    }

    private void calculate_profit() {
        Profit = 0.10 * Cost; // 10% profit margin
    }

    public static void main(String[] args) {
        Product product = new Product();

        System.out.println("Enter product details:");
        product.Set_Data();

        System.out.println("\nProduct details:");
        product.Print_Data();
    }
}
