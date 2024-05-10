class Solution {
    public long solution(long n) {
        long answer = 0;
        
        for (long i =0; i <=  500000000; i++) {
            if (n == (i*i)) {
                answer = (i+1)*(i+1);
                break;
            } else {
                answer = -1;
            }
        }
        
        return answer;
    }
}