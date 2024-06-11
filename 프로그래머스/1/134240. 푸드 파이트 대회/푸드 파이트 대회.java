class Solution {
    public String solution(int[] food) {
        int length = 0;
        StringBuilder sb = new StringBuilder();
        
        for(int i = 1; i < food.length; i++) {
            int index = food[i] / 2;
            
            if(index >= 1) {
            String str = String.valueOf(i);
            sb.append(str.repeat(index));
            }
        }
        
        
        String answer = sb.toString() + "0" + sb.reverse().toString();
        return answer;
    }
}