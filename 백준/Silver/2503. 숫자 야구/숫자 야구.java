import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        int[][] arr = new int[n][3];
        for(int i = 0; i < n; i++) {
            arr[i][0] = sc.nextInt();
            arr[i][1] = sc.nextInt();
            arr[i][2] = sc.nextInt();
        }
        sc.close();

        int answer = 0;
        for(int i = 123; i <= 987; i++) {
            String numStr = Integer.toString(i);

            if (numStr.charAt(0) == numStr.charAt(1) ||
                    numStr.charAt(1) == numStr.charAt(2) ||
                    numStr.charAt(0) == numStr.charAt(2)) {
                continue;
            }

            if (numStr.charAt(0) == '0' ||
                    numStr.charAt(1) == '0' ||
                    numStr.charAt(2) == '0') {
                continue;
            }

            boolean flag = true;
            for (int[] ints : arr) {
                int arrNum = ints[0];
                int arrStrike = ints[1];
                int arrBall = ints[2];

                String arrNumStr = Integer.toString(arrNum);

                int strike = 0;
                int ball = 0;

                for(int j = 0; j < 3; j++) {
                    if (arrNumStr.charAt(j) == numStr.charAt(j)) strike++;
                }

                for(int j = 0; j < 3; j++) {
                    if (arrNumStr.charAt(j) != numStr.charAt(j) &&
                            numStr.contains(arrNumStr.charAt(j) + "")) {
                        ball++;
                    }
                }


                if(strike != arrStrike || ball != arrBall) {
                    flag = false;
                    break;
                }
            }

            if(flag) answer++;
        }

        System.out.println(answer);


    }

}