import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static int answer = 0;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String givenStr = sc.nextLine();

        HashMap<Character, Integer> map = new HashMap<>();

        for (int i = 0; i < givenStr.length(); i++) {
            map.put(givenStr.charAt(i), map.getOrDefault(givenStr.charAt(i), 0) + 1);
        }

        char[] charArr = new char[map.size()];
        int[] countArr = new int[map.size()];
        int index = 0;
        for (Character c : map.keySet()) {
            charArr[index] = c;
            countArr[index] = map.get(c);
            index++;
        }

        makeLuckyStr(charArr, countArr, givenStr, "");
        System.out.println(answer);

    }

    public static void makeLuckyStr(char[] charArr, int[] countArr, String givenStr, String luckyStr) {
            if (luckyStr.length() == givenStr.length()) {
                makeAnswer(luckyStr);
                return;
            }

            for (int i = 0; i < charArr.length; i++) {
                if (countArr[i] > 0) {
                    if (luckyStr.length() == 0 || luckyStr.charAt(luckyStr.length() - 1) != charArr[i]) {
                        countArr[i]--;
                        makeLuckyStr(charArr, countArr, givenStr, luckyStr + charArr[i]);
                        countArr[i]++;  // 백트래킹
                    }
                }
            }
    }

    public static void makeAnswer(String luckyStr) {
        boolean flag = true;

        for (int i = 1; i < luckyStr.length(); i++) {
            if(luckyStr.charAt(i) == luckyStr.charAt(i-1)) {
                flag = false;
                break;
            }
        }

        if(flag) answer++;
    }
}

