import java.util.PriorityQueue;

class Solution {
    public int[] solution(int k, int[] score) {
        
        PriorityQueue<Integer> pQ = new PriorityQueue<>(k);
        int[] answer = new int[score.length];
        
        for(int i = 0; i < score.length; i ++) {
            if (i < k) {
                pQ.offer(score[i]);
                answer[i] = pQ.peek();
            } else {
                if (pQ.peek()<score[i]) {
                pQ.poll();
                pQ.offer(score[i]);
                answer[i] = pQ.peek(); 
                } else {
                    answer[i] = pQ.peek(); 
                }
            }
        }
        
        return answer;
    }
}