class Solution {
    public long solution(int price, int money, int count) {
        long sum=0;
        for(int i = 1; i <= count; i++) {
            sum += price * i;
        }
        long answer = (sum-money > 0) ? sum - money : 0;

        return answer;
    }
}