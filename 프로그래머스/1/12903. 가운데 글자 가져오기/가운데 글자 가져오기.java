class Solution {
    public String solution(String s) {
        int sLength = s.length();
        String s1 = "";
        if (sLength%2 == 0) {
            //짝수라면
            s1 = s.substring(sLength/2-1, sLength/2+1);
        } else {
            //홀수라면
            s1 = s.substring(sLength/2, sLength/2+1);
        }
        return s1;
        
        
        // char[] charArr = s.toCharArray();
        // int charArrSize = charArr.length;
        // String answer = "";
        // switch(charArrSize%2){
        //         case 0 -> 
        //             answer = String.valueOf(charArr[charArrSize/2-1]) + String.valueOf(charArr[charArrSize/2]);
        //         case 1 -> 
        //             answer = String.valueOf(charArr[charArrSize/2]);
        // }
        // return answer;
    }
}