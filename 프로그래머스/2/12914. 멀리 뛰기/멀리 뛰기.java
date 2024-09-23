class Solution {
    public long solution(int n) {
        // n이 1이면 방법은 1개
        if (n == 1) return 1;
        
        // DP 배열 선언
        long[] dp = new long[n + 1];
        dp[1] = 1;
        dp[2] = 2;

        // DP로 문제 해결
        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567;
        }
        
        return dp[n];
    }
}
