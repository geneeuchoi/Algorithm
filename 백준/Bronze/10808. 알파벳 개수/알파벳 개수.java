import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inputStr = sc.nextLine();
        int[] arr = new int[26];

        for (int i = 0; i < inputStr.length(); i++) {
            int index = inputStr.charAt(i) - 'a';
            arr[index]++;
        }

        for (int i : arr) {
            System.out.print(i + " ");
        }

    }
}