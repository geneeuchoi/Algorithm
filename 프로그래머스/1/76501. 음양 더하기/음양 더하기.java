class Solution {
    public int solution(int[] absolute, boolean[] signs) {
        int answer = 0;
        for(int i = 0; i < absolute.length; i++) {
            if(signs[i] == true) {
                answer = answer + absolute[i];
            } else {
                answer = answer - absolute[i];
            }
        }
        
        return answer;
    }
}