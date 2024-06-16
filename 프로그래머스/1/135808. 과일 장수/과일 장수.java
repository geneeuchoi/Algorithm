import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        Arrays.sort(score);
        
        int sum = 0;
        int tmp = score.length;
        
        if(score.length < m) {
            return 0;
        } else {
            while(tmp >= m) {
                sum += score[tmp - m] * m;
                tmp -= m;
            }
            return sum;
        }
    }
}