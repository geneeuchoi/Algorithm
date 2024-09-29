import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String num = sc.nextLine();
        int answer = 0;

        for (int i = 1; i <1000001; i++) {
            answer = 0;
            String iStr = Integer.toString(i);
            for(int j = 0; j < iStr.length(); j++){
                answer += iStr.charAt(j)-'0';
            }
            answer += i;

            if(num.equals(Integer.toString(answer))) {
                answer = i;
                break;
            }
        }

        answer = (answer == 1000001)? 0 : answer;
        System.out.println(answer);

    }
}