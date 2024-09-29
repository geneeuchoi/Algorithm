import java.util.Arrays;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[9];
        int sum = 0;
        for(int i = 0; i < 9; i++) {
            arr[i] = sc.nextInt();
            sum += arr[i];
        }

        int except = sum - 100;
        int value1 = 0;
        int value2 = 0;
        for(int i = 0; i < 9; i++) {
            for(int j = i + 1; j < 9; j++) {
                if(arr[i]+ arr[j] == except) {
                    value1 = arr[i];
                    value2 = arr[j];
                    break;
                }
            }
        }

        int[] answer = new int[7];
        int answerIndex = 0;
        for (int i : arr) {
            if (i != value1 && i != value2) {
                answer[answerIndex] = i;
                answerIndex++;
            }
        }

        Arrays.sort(answer);
        for (int i : answer) {
            System.out.println(i);
        }
    }
}