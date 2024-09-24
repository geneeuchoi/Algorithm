class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i = 1; i <= n; i++) {
            answer++;
            boolean flag = true;
            while(flag) {
                String answerStr = Integer.toString(answer);
                if(answer % 3 == 0 || answerStr.contains("3")) answer++;
                else flag = false;
            }
        }
        return answer;
    }
}