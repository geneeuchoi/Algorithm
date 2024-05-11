import java.util.*;
import java.io.*;

class Solution {
    public long solution(long n) {
        String nString = "" + n;
        char[] nCharArr = nString.toCharArray();
        String[] nArr = new String[nCharArr.length];
        int i =0;
        for (char nChar : nCharArr) {
            nArr[i] = String.valueOf(nChar);
            i++;
        }
        Arrays.sort(nArr, Collections.reverseOrder());
        
        String strAnswer = "";
        StringBuilder sb = new StringBuilder();
        for (String s : nArr) {
            strAnswer = sb.append(s).toString();
        }
        
        long answer = Long.valueOf(strAnswer);
        return answer;
    }
}