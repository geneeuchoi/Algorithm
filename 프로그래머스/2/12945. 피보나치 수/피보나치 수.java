import java.util.*;

class Solution {
    public int solution(int n) {
        List<Integer> fib = new ArrayList<>();
        
        fib.add(0);
        fib.add(1);
        
        for(int i = 2; i <= n; i++) {
            int addedValue = (fib.get(i-1) + fib.get(i-2)) % 1234567;
            fib.add(addedValue);
        }
        
        return fib.get(n);
    }
}