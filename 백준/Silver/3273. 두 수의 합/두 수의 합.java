import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        sc.nextLine();

        int x = sc.nextInt();
        sc.close();

        int answer = 0;
        for (int i = 0; i < n; i++) {
            int anotherNum = x - arr[i];
            for (int j = i + 1; j < n; j++) {
                if (anotherNum == arr[j]) {
                    answer++;
                    break;
                }
            }
        }
        System.out.println(answer);
    }
}