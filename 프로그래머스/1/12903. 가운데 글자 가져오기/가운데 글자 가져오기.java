class Solution {
    public String solution(String s) {
        char[] charArr = s.toCharArray();
        int charArrSize = charArr.length;
        String answer = "";
        switch(charArrSize%2){
                case 0 -> 
                    answer = String.valueOf(charArr[charArrSize/2-1]) + String.valueOf(charArr[charArrSize/2]);
                case 1 -> 
                    answer = String.valueOf(charArr[charArrSize/2]);
        }
        return answer;
    }
}