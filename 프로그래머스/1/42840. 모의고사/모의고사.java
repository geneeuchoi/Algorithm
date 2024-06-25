import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] answers) {
        int[] student1 = {1, 2, 3, 4, 5};
        int[] student2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] student3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] score = {0, 0, 0};
        
        int j = 0;
        
        for(int answer : answers) {
            score[0] += student1[j%5] == answer? 1 : 0;
            score[1] += student2[j%8] == answer? 1 : 0;
            score[2] += student3[j%10] == answer? 1 : 0;
            j++;
        }
        
        int max =  Math.max(score[0], Math.max(score[1], score[2]));
        
        List<Integer> maxList = new ArrayList<>();
        
        for(int i = 0 ; i < 3 ; i++) {
            if (max == score[i]) {
                maxList.add(i+1);
            }
        }
        
        int[] answer = new int[maxList.size()];
        for(int i=0; i<maxList.size(); i++){
            answer[i] = maxList.get(i);
        }

        return answer;
    }
}