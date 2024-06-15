package zoo_maintains_details;
import java.util.HashMap;
import java.util.Scanner;
class Zoo {
    private HashMap<String, String> employee;

    public Zoo() {
        employee = new HashMap<>();
        employee.put("John Doe", "Caretaker");
        employee.put("Jane Smith", "Doctor");
        employee.put("Bob Brown", "MedicalAssistant");
        employee.put("Dr. Brown", "Doctor");
        employee.put("Anna Smith","Caretaker");
        employee.put("Mike Johnson","MedicalAssistant");
    }

    public void add_employee(String name, String work) {
        employee.put(name, work);
    }

    public HashMap<String, String> getEmployee() {
        return employee;
    }

}

class Caretakers {
    public Zoo name=new Zoo();

    public void details() {
        HashMap<String, String> caretakers = name.getEmployee();
        for (HashMap.Entry<String, String> entry : caretakers.entrySet()) {
            if (entry.getValue().equals("Caretaker")) {
                System.out.println(entry.getKey()+" (Caretaker)");
            }
        }
    }
}
class Doctors extends Caretakers{
	public void details() {
        HashMap<String, String> doctors = name.getEmployee();
        for (HashMap.Entry<String, String> entry : doctors.entrySet()) {
            if (entry.getValue().equals("Doctor")) {
                System.out.println(entry.getKey()+"(Doctor)");
            }
        }
    }
}
class MedicalAssistants extends Caretakers{
	public void details() {
        HashMap<String, String> medicalAssistant = name.getEmployee();
        for (HashMap.Entry<String, String> entry : medicalAssistant.entrySet()) {
            if (entry.getValue().equals("MedicalAssistant")) {
                System.out.println(entry.getKey()+" (MedicalAssistant)");
            }
        }
    }
}
class Animal {
    private String name;
    private String doctor;
    private String caretaker;
    private String medicalAssistant;
    private String food;
    private String medicine;

    public Animal(String name, String doctor, String caretaker, String medicalAssistant, String food, String medicine) {
        this.name = name;
        this.doctor = doctor;
        this.caretaker = caretaker;
        this.medicalAssistant = medicalAssistant;
        this.food = food;
        this.medicine = medicine;
    }

    public void printDetails() {
        System.out.println("Name: " + name);
        System.out.println("Doctor: " + doctor);
        System.out.println("Caretaker: " + caretaker);
        System.out.println("Medical Assistant: " + medicalAssistant);
        System.out.println("Food: " + food);
        System.out.println("Medicine: " + medicine);
        System.out.println("---------------------------------------------");
    }
}

class Lion extends Animal {
    public Lion(String name, String doctor, String caretaker, String medicalAssistant, String food, String medicine) {
        super(name, doctor, caretaker, medicalAssistant, food, medicine);
    }
}

class Elephant extends Animal {
    public Elephant(String name, String doctor, String caretaker, String medicalAssistant, String food, String medicine) {
        super(name, doctor, caretaker, medicalAssistant, food, medicine);
    }
}
public class test {
    public static void main(String[] args) {
    	
        Scanner scanner = new Scanner(System.in);
        String continueChoice;
        Caretakers obj1=new Caretakers();
        Doctors obj2=new Doctors();
        MedicalAssistants obj3=new MedicalAssistants();
        do {
            System.out.println("-------------Zoo-----------");
            System.out.println("Available animals:");
            System.out.println("Lion, Elephant");
            System.out.println("Type (Lion) to get details of lion and (Elephant) to get details of Elephant");
            System.out.println("*****************************");
            System.out.println("Available employees");
            System.out.println("Doctor,Caretaker,MedicalAssistant");
            System.out.println("Type (Doctor)to get details of doctor");
            System.out.println("Type (MedicalAssitant)to get details of MedicalAssistant");
            System.out.println("Type (Caretaker)to get details of Caretaker");
            System.out.println("*****************************");
            String animalChoice = scanner.next();
            String employeeChoice=scanner.next();
            if ("Lion".equals(animalChoice)) {
                Lion lion = new Lion("Simba", "Jane Smith", "John Doe", "Bob Brown", "Meat", "Painkillers");
                lion.printDetails();
            } else if ("Elephant".equals(animalChoice)) {
                Elephant elephant = new Elephant("Dumbo", "Dr. Brown", "Anna Smith", "Mike Johnson", "Vegetables", "Antibiotics");
                elephant.printDetails();
            } else if("Doctor".equals(employeeChoice)) {
            	obj2.details();
            }else if("Caretaker".equals(employeeChoice)) {
            	obj1.details();
            }else if("MedicalAssistant".equals(employeeChoice)) {
            	obj3.details();
            }
            else {
                System.out.println("Invalid animal choice!");
            }

            System.out.println("Do you want to continue? (Yes/No)");
            continueChoice = scanner.next();
        } while ("Yes".equals(continueChoice));

        System.out.println("Exiting program.");
        scanner.close();
    }
}
