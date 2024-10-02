import java.util.Scanner;

public class Main {
    static int N, S;
    static int[] arr;
    static int count = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        S = sc.nextInt();
        arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        sc.close();

        // 부분수열을 탐색하는 함수 호출
        findSubsequences(0, 0);

        // S가 0일 때는 공집합을 제외해야 하므로 1을 빼줌
        if (S == 0) count--;

        System.out.println(count);
    }

    // index번째 원소를 포함할지 말지 결정하면서 부분수열을 탐색하는 함수
    public static void findSubsequences(int index, int sum) {
        // 모든 원소를 탐색한 경우
        if (index == N) {
            if (sum == S) {
                count++;
            }
            return;
        }

        // 현재 원소를 포함하지 않는 경우
        findSubsequences(index + 1, sum);

        // 현재 원소를 포함하는 경우
        findSubsequences(index + 1, sum + arr[index]);
    }
}
