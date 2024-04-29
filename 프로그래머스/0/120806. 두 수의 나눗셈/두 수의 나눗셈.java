class Solution {
    public int solution(int num1, int num2) {
        int num3 = num1 % num2;
        double num4 = num1 / num2;
        for (int i = 1; i < 4; i++) {
            if (num3 != 0) {
             num3 = num3 * 10 / num2;
             double num5 = num4 + num3 * Math.pow(0.1, i);
            }   
        }
         
        int result = num5 * 1000;
        return result;
    }
}