class Solution {
    public int[] solution(int num, int total) {
        int startNum = (total / num) - ((num-1)/2);
        int[] answer = new int[num];
        
        for(int i = 0; i < num; i++) {
            answer[i] = startNum;
            startNum++;
        }
        
        return answer;
    }
}