import java.util.HashMap;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int cost = sc.nextInt();
        int rest = 1000 - cost;

        int answer = 0;
        int[] restArr = {500, 100, 50, 10, 5, 1};

        for (int coin : restArr) {
            int count = rest / coin;
            answer += count;
            rest -= coin * count;
        }
        System.out.println(answer);

    }
}

