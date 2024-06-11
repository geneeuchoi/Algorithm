class Solution {
    public int[] solution(String s) {
        //answer 배열 생성
        int[] answer = new int[s.length()];
        
        for (int i = s.length()-1; i >= 0; i--) {
            if (i == 0) {
                answer[i] = -1;
            }
            for(int j = i-1; j >= 0; j--) {
                
                if (s.charAt(i) == s.charAt(j)){
                    answer[i] = i-j;
                    break;
                } else {
                    answer[i] = -1;
                }
                
            }
        }
        return answer;
    }
}