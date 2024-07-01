import java.util.*;
class Solution {
    public String solution(String s, String skip, int index) {
        char[] sArr = s.toCharArray();
        Set<Character> skipSet = new HashSet<>();
        for (char skipChar : skip.toCharArray()) {
            skipSet.add(skipChar);
        }

        StringBuilder sb = new StringBuilder();

        for (char sChar : sArr) {
            int moves = 0;
            char newChar = sChar;

            while (moves < index) {
                newChar++;
                if (newChar > 'z') {
                    newChar = 'a';
                }
                if (!skipSet.contains(newChar)) {
                    moves++;
                }
            }
            
            sb.append(newChar);
        }

        return sb.toString();
    }
}
