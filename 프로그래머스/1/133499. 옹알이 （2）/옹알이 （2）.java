class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        for(String str: babbling) {
            if(!str.contains("ayaaya") && !str.contains("yeye") && 
               !str.contains("woowoo") && !str.contains("mama")) {
                String str1 = str.replace("aya", " ");
                String str2 = str1.replace("ye", " ");
                String str3 = str2.replace("woo", " ");
                String str4 = str3.replace("ma", " ");
                
                answer += str4.isBlank()? 1: 0;
            }
        }
        
        return answer;
    }
}