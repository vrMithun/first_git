import java.util.Arrays;

// Person class as an abstract class
abstract class Person {
    protected String ID;
    protected String Name;
    protected int Age;
    protected String Occupation;
    protected String BankAccno;

    // Constructor
    public Person(String id, String name, int age, String occupation, String bankAccno) {
        this.ID = id;
        this.Name = name;
        this.Age = age;
        this.Occupation = occupation;
        this.BankAccno = bankAccno;
    }

    // Abstract method
    abstract void cal_monthly_income();

    // Getters and setters
    public String getID() {
        return ID;
    }

    public void setID(String iD) {
        ID = iD;
    }

    public String getName() {
        return Name;
    }

    public void setName(String name) {
        Name = name;
    }

    public int getAge() {
        return Age;
    }

    public void setAge(int age) {
        Age = age;
    }

    public String getOccupation() {
        return Occupation;
    }

    public void setOccupation(String occupation) {
        Occupation = occupation;
    }

    public String getBankAccno() {
        return BankAccno;
    }

    public void setBankAccno(String bankAccno) {
        BankAccno = bankAccno;
    }
}

// Farmer class extending Person
class Farmer extends Person {
    protected double land_area;
    protected double income;

    // Constructor
    public Farmer(String id, String name, int age, String occupation, String bankAccno, double land_area) {
        super(id, name, age, occupation, bankAccno);
        this.land_area = land_area;
    }

    // Implementing abstract method
    @Override
    void cal_monthly_income() {
        if (land_area > 10)
            income = 10000 * land_area;
        else
            income = 3000;
    }

    // Getters and setters
    public double getLand_area() {
        return land_area;
    }

    public void setLand_area(double land_area) {
        this.land_area = land_area;
    }

    public double getIncome() {
        return income;
    }

    public void setIncome(double income) {
        this.income = income;
    }
}

// Employee class extending Person
class Employee extends Person {
    protected double sal;
    protected int experience;
    protected double bonus;
    protected double Total_salary;

    // Constructor
    public Employee(String id, String name, int age, String occupation, String bankAccno, double sal, int experience,
            double bonus) {
        super(id, name, age, occupation, bankAccno);
        this.sal = sal;
        this.experience = experience;
        this.bonus = bonus;
    }

    // Implementing abstract method
    @Override
    void cal_monthly_income() {
        Total_salary = sal * experience + (experience / 2) * bonus;
    }

    // Getters and setters
    public double getSal() {
        return sal;
    }

    public void setSal(double sal) {
        this.sal = sal;
    }

    public int getExperience() {
        return experience;
    }

    public void setExperience(int experience) {
        this.experience = experience;
    }

    public double getBonus() {
        return bonus;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

    public double getTotal_salary() {
        return Total_salary;
    }

    public void setTotal_salary(double total_salary) {
        Total_salary = total_salary;
    }
}

// Interface for Farmer-Market
interface FarmerMarket {
    void SubsidyCalculator();

    void InsuranceCalculator();

    void LoanCalculator();
}

// ArgilandEntrepreneurship class
class ArgilandEntrepreneurship extends Farmer implements FarmerMarket {
    private String farmland_id;
    private String location;
    private String crops_grown;
    private double subsidy;
    private double insurance;
    private double loan;

    // Constructor
    public ArgilandEntrepreneurship(String id, String name, int age, String occupation, String bankAccno,
            double land_area, String farmland_id, String location, String crops_grown) {
        super(id, name, age, occupation, bankAccno, land_area);
        this.farmland_id = farmland_id;
        this.location = location;
        this.crops_grown = crops_grown;
    }

    // Implementing interface methods
    @Override
    public void SubsidyCalculator() {
        if (income == 3000)
            subsidy = income * 0.5;
        else
            subsidy = income * 0.2;
    }

    @Override
    public void InsuranceCalculator() {
        if (land_area < 10)
            insurance = 10000;
        else
            insurance = 20000;
    }

    @Override
    public void LoanCalculator() {
        if (land_area > 10)
            loan = land_area * 10000;
        else
            loan = 50000;
    }

    // Getters and setters
    public String getFarmland_id() {
        return farmland_id;
    }

    public void setFarmland_id(String farmland_id) {
        this.farmland_id = farmland_id;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getCrops_grown() {
        return crops_grown;
    }

    public void setCrops_grown(String crops_grown) {
        this.crops_grown = crops_grown;
    }

    public double getSubsidy() {
        return subsidy;
    }

    public void setSubsidy(double subsidy) {
        this.subsidy = subsidy;
    }

    public double getInsurance() {
        return insurance;
    }

    public void setInsurance(double insurance) {
        this.insurance = insurance;
    }

    public double getLoan() {
        return loan;
    }

    public void setLoan(double loan) {
        this.loan = loan;
    }
}

// AgriBasedFoodCompanies class
class AgriBasedFoodCompanies implements FarmerMarket {
    public String company_id; // Change to public visibility
    private String name;
    private String category;
    private Employee[] employees;
    private double net_worth;
    private double subsidy;
    private double insurance;
    private double loan;

    // Constructor
    public AgriBasedFoodCompanies(String company_id, String name, String category, Employee[] employees,
            double net_worth) {
        this.company_id = company_id;
        this.name = name;
        this.category = category;
        this.employees = employees;
        this.net_worth = net_worth;
    }

    // Implementing interface methods
    @Override
    public void SubsidyCalculator() {
        if (net_worth == 100000)
            subsidy = net_worth * 0.2;
        else
            subsidy = net_worth * 0.1;
    }

    @Override
    public void InsuranceCalculator() {
        if (category.equals("NGO"))
            insurance = 10000;
        else
            insurance = net_worth * 10;
    }

    @Override
    public void LoanCalculator() {
        double totalSalaries = Arrays.stream(employees).mapToDouble(emp -> emp.Total_salary).sum();
        if (totalSalaries > 20000 * employees.length)
            loan = employees.length * 10000;
        else
            loan = 0;
    }

    // Getters and setters
    public String getCompany_id() {
        return company_id;
    }

    public void setCompany_id(String company_id) {
        this.company_id = company_id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public Employee[] getEmployees() {
        return employees;
    }

    public void setEmployees(Employee[] employees) {
        this.employees = employees;
    }

    public double getNet_worth() {
        return net_worth;
    }

    public void setNet_worth(double net_worth) {
        this.net_worth = net_worth;
    }

    public double getSubsidy() {
        return subsidy;
    }

    public void setSubsidy(double subsidy) {
        this.subsidy = subsidy;
    }

    public double getInsurance() {
        return insurance;
    }

    public void setInsurance(double insurance) {
        this.insurance = insurance;
    }

    public double getLoan() {
        return loan;
    }

    public void setLoan(double loan) {
        this.loan = loan;
    }
}

public class Main {
    // Static block example
    static {
        System.out.println("Welcome to the Agri Portal System!");
    }

    // Dynamic dispatch example
    public static void main(String[] args) {
        // Create a farmer object
        Farmer farmer1 = new Farmer("F1", "John Doe", 35, "Farmer", "12345", 15);
        farmer1.cal_monthly_income(); // Calculate monthly income for the farmer

        // Create an employee object
        Employee employee1 = new Employee("E1", "Jane Smith", 28, "Manager", "67890", 5000, 5, 2000);
        employee1.cal_monthly_income(); // Calculate monthly salary for the employee

        // Print details of the farmer
        System.out.println("Farmer Details:");
        System.out.println("ID: " + farmer1.getID());
        System.out.println("Name: " + farmer1.getName());
        System.out.println("Age: " + farmer1.getAge());
        System.out.println("Occupation: " + farmer1.getOccupation());
        System.out.println("Bank Account Number: " + farmer1.getBankAccno());
        System.out.println("Land Area: " + farmer1.getLand_area() + " acres");
        System.out.println("Monthly Income: $" + farmer1.getIncome());

        System.out.println(); // Blank line for separation

        // Print details of the employee
        System.out.println("Employee Details:");
        System.out.println("ID: " + employee1.getID());
        System.out.println("Name: " + employee1.getName());
        System.out.println("Age: " + employee1.getAge());
        System.out.println("Occupation: " + employee1.getOccupation());
        System.out.println("Bank Account Number: " + employee1.getBankAccno());
        System.out.println("Salary: $" + employee1.getSal());
        System.out.println("Experience: " + employee1.getExperience() + " years");
        System.out.println("Bonus: $" + employee1.getBonus());
        System.out.println("Total Monthly Salary: $" + employee1.getTotal_salary());

        System.out.println(); // Blank line for separation

        // Create an Agri-based food company object
        Employee[] employees = { employee1 }; // Array of employees for the company
        AgriBasedFoodCompanies company1 = new AgriBasedFoodCompanies("C1", "ABC Foods", "NGO", employees, 150000);
        company1.SubsidyCalculator(); // Calculate subsidy for the company
        company1.InsuranceCalculator(); // Calculate insurance for the company
        company1.LoanCalculator(); // Calculate loan for the company

        // Print details of the company
        System.out.println("Company Details:");
        System.out.println("ID: " + company1.getCompany_id());
        System.out.println("Name: " + company1.getName());
        System.out.println("Category: " + company1.getCategory());
        System.out.println("Net Worth: $" + company1.getNet_worth());
        System.out.println("Subsidy: $" + company1.getSubsidy());
        System.out.println("Insurance: $" + company1.getInsurance());
        System.out.println("Loan: $" + company1.getLoan());

        System.out.println(); // Blank line for separation

        // Create an Argiland-entrepreneurship object
        ArgilandEntrepreneurship farm1 = new ArgilandEntrepreneurship("F2", "Farm Enterprises", 40, "Farmer", "54321",
                8, "F-001", "Rural", "Wheat");
        farm1.cal_monthly_income(); // Calculate monthly income for the farm
        farm1.SubsidyCalculator(); // Calculate subsidy for the farm
        farm1.InsuranceCalculator(); // Calculate insurance for the farm
        farm1.LoanCalculator(); // Calculate loan for the farm

        // Print details of the farm
        System.out.println("Farm Details:");
        System.out.println("ID: " + farm1.getID());
        System.out.println("Name: " + farm1.getName());
        System.out.println("Age: " + farm1.getAge());
        System.out.println("Occupation: " + farm1.getOccupation());
        System.out.println("Bank Account Number: " + farm1.getBankAccno());
        System.out.println("Land Area: " + farm1.getLand_area() + " acres");
        System.out.println("Farmland ID: " + farm1.getFarmland_id());
        System.out.println("Location: " + farm1.getLocation());
        System.out.println("Crops Grown: " + farm1.getCrops_grown());
        System.out.println("Subsidy: $" + farm1.getSubsidy());
        System.out.println("Insurance: $" + farm1.getInsurance());
        System.out.println("Loan: $" + farm1.getLoan());
    }
}
