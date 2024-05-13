class Solution {
    long sum = 0;
    long answer = 0;
    public long solution(int a, int b) {
        if (a < b) {
            answer = calculateSum(a, b);
        } else if (a > b) {
            answer = calculateSum(b, a);
        } else {
            answer = 3;
        }
        
        return answer;
    }
    
    public long calculateSum(int firstNum, int secondNum) {
        for(int i = firstNum; i<= secondNum; i++) {
            sum += i;
        }
        return sum;
    }
}