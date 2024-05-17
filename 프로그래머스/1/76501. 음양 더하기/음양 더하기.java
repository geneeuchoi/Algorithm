class Solution {
    public int solution(int[] absolute, boolean[] signs) {
        int answer = 0;
        
        for(int i = 0; i < absolute.length; i++) {
            answer = signs[i] == true ? answer + absolute[i] : answer - absolute[i];
        }
        
        return answer;
    }
}