class Solution {
    public int solution(int num1, int num2) {
        double result = num1 / num2;
        int nam = num1 % num2;
        for (int i = 1; i < 4; i++) {
            if (nam != 0) {
                num1 = nam * 10;
                result += num1 / num2 * Math.pow(0.1, i);
                nam = num1 % num2;
            } else {
                break;
            }
        }
        int returnResult = (int)Math.round(result*1000);
        return returnResult;
    }
}