class Solution {
    public boolean solution(int x) {
        String[] strArr = String.valueOf(x).split("");
        int sum = 0;
        
        for (String element : strArr) {
            int elementValue = Integer.parseInt(element);
            sum += elementValue;
        }
        
        boolean answer;
        if (x % sum == 0) {
         answer = true;   
        } else {
            answer = false;
        }
        return answer;
    }
}