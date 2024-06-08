class Solution {
    public String solution(String s, int n) {
        //소문자 97~122
        //대문자 65~90
        //공백 32
        StringBuilder sb = new StringBuilder(); 
        
        for(int i = 0; i < s.length() ; i++) {
            char sChar = s.charAt(i);
            int num = Integer.valueOf(sChar);
            if(97<=num && num <= 122){
                num += n;
                if (num > 122) {
                num = num-123+97;
                }
            } else if(65<=num && num <= 90) {
                num += n;
                if(num > 90) {
                    num = num-91+65;
                } 
            }
            char str = (char) num;
            sb.append(str);
        }
        return sb.toString();
    }
}