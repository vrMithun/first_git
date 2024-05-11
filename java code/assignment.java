import java.util.ArrayList;
import java.util.List;

class Equipment {
    private String type;

    public Equipment(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }

    @Override
    public String toString() {
        return "Equipment Type: " + type;
    }
}

class ProjectMember {
    private String type;
    private String name;

    public ProjectMember(String type, String name) {
        this.type = type;
        this.name = name;
    }

    public String getType() {
        return type;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "Project Member Type: " + type + ", Name: " + name;
    }
}

class Project {
    private int id;
    private String title;
    private double totalBudget;
    private int totalMembers;
    private int totalEquipments;
    private List<ProjectMember> members;
    private List<Equipment> equipments;

    public Project(int id, String title, double totalBudget, int totalMembers, int totalEquipments) {
        this.id = id;
        this.title = title;
        this.totalBudget = totalBudget;
        this.totalMembers = totalMembers;
        this.totalEquipments = totalEquipments;
        members = new ArrayList<>();
        equipments = new ArrayList<>();
    }

    public void addMember(ProjectMember member) {
        members.add(member);
    }

    public void addEquipment(Equipment equipment) {
        equipments.add(equipment);
    }

    public void displayDetails() {
        System.out.println("Project ID: " + id);
        System.out.println("Title: " + title);
        System.out.println("Total Budget: " + totalBudget);
        System.out.println("Total Members: " + totalMembers);
        System.out.println("Total Equipments: " + totalEquipments);
        System.out.println("Project Members:");
        for (ProjectMember member : members) {
            System.out.println(member);
        }
        System.out.println("Equipments:");
        for (Equipment equipment : equipments) {
            System.out.println(equipment);
        }
    }
}

public class assignment {
    public static void main(String[] args) {
        Project project1 = new Project(1, "Research Project 1", 10000, 5, 3);
        project1.addMember(new ProjectMember("Coordinator", "John Doe"));
        project1.addMember(new ProjectMember("Intern", "Jane Smith"));
        project1.addMember(new ProjectMember("Researcher", "David Brown"));
        project1.addEquipment(new Equipment("Hardware"));
        project1.addEquipment(new Equipment("Software"));
        project1.addEquipment(new Equipment("Software"));

        Project project2 = new Project(2, "Research Project 2", 15000, 7, 4);
        project2.addMember(new ProjectMember("Faculty", "Emily Johnson"));
        project2.addMember(new ProjectMember("Researcher", "Michael Wilson"));
        project2.addEquipment(new Equipment("Hardware"));
        project2.addEquipment(new Equipment("Software"));
        project2.addEquipment(new Equipment("Hardware"));
        project2.addEquipment(new Equipment("Hardware"));

        project1.displayDetails();
        System.out.println("------------------------");
        project2.displayDetails();
    }
}
