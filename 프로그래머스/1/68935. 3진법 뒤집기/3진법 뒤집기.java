import java.util.ArrayList;

class Solution {
    public int solution(int n) {
        ArrayList<Integer> numList = new ArrayList<>();
        
        int a = n;
        
        while(a/3 != 0) {
            int b = a % 3;
            a = a / 3;
            numList.add(b);
        }
        numList.add(a);
        
        
        int result = 0;
        for(int i = 0; i <= numList.size()-1; i++) {
            result += numList.get(i) * Math.pow(3, numList.size()-1-i);
        }
        
        return result;
    }
}