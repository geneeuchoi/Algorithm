class Solution {
    boolean solution(String s) {
        int[] countList = new int[2];
        
        for(int i = 0; i<s.length(); i++) {
            if(s.charAt(i) == 'P' || s.charAt(i) == 'p') countList[0]++;
            if(s.charAt(i) == 'Y' || s.charAt(i) == 'y') countList[1]++;
        }
        
        
        boolean answer = (countList[0] == countList[1])? true : false;

        return answer;
    }
}