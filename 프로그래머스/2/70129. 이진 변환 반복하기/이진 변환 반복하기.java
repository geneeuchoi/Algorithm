class Solution {
    public int[] solution(String s) {
        int round = 0;
        int removedZero = 0;
        
        // 1이 될 때까지 반복
        while(!s.equals("1")) {
            int afterLength = 0;
            
            for(int i = 0; i < s.length(); i++) {
                removedZero += s.charAt(i) == '0'? 1 : 0;
                afterLength += s.charAt(i) == '1'? 1 : 0;
            }
            
            // afterLength를 이진수로 변환
            StringBuilder sb = new StringBuilder();
            while (afterLength > 0) {
                sb.append(afterLength % 2);
                afterLength /= 2;
            }
            
            // 변환된 이진수를 다시 s로 설정
            s = sb.reverse().toString();
            
            round++;
        }
        
        int[] answer = {round, removedZero};
        return answer;
    }
}