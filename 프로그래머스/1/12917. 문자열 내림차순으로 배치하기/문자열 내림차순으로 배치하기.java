import java.util.Arrays;
import java.util.Collections;
class Solution {
    public String solution(String s) {
        Character[] charArr = new Character[s.length()];
        for (int i = 0; i < s.length(); i++) {
            charArr[i] = s.charAt(i);
        }
        Arrays.sort(charArr, Collections.reverseOrder());
        StringBuilder sb = new StringBuilder(charArr.length);
        for (Character c : charArr) {
            sb.append(c);
        }

        return sb.toString();
    }
}