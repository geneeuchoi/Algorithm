import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        
        int[] gamers = new int[N+1];
        
        for(int i = 0; i < stages.length; i++) {
            gamers[stages[i]-1] += 1;
        }
        
        float[] failRate = new float[N];
        int totalGamers = stages.length;
        for(int i = 0; i < gamers.length-1; i++) {
            if (totalGamers == 0) {
                failRate[i] = 0;
            } else {
                failRate[i] = (float) gamers[i] / totalGamers;
                totalGamers -= gamers[i];
            }
        }
        
        float[] orderedFailRate = Arrays.copyOf(failRate, failRate.length);
        Arrays.sort(orderedFailRate);
        
        
        int[] answer = new int[N];
        boolean[] answerFlag = new boolean[N];
        int answerIndex = 0;
        
        for(int i = orderedFailRate.length-1; i >= 0; i--) {
            for(int j = 0; j < failRate.length; j++) {
                if(orderedFailRate[i] == failRate[j] && !answerFlag[j]) {
                    answer[answerIndex] = j+1;
                    answerFlag[j] = true;
                    answerIndex++;
                    break;
                }
            }
        }
        return answer;
    }
}