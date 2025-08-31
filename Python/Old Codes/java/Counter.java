public class Counter {
  public static int classCount = 0; 
  public void fun(int i){
    classCount=i;
    System.out.println(classCount);
  }
  public static void main(String[] args){
    Counter obj=new Counter();
    obj.fun(5);
    obj.fun(7);
  }
  }