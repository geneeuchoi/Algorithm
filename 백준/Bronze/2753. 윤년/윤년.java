import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();

        boolean flag = ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))? true : false;
        int answer = flag? 1 : 0;

        System.out.println(answer);

    }
}