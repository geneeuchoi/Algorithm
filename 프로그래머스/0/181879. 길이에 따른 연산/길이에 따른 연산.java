class Solution {
    public int solution(int[] num_list) {
        if(num_list.length >= 11) {
            int sum = 0;
            for(int i : num_list) {
                sum += i;
            }
            return sum;
        } else {
            int sum = 1;
            for(int i : num_list) {
                sum *= i;
            }
            return sum;
        }
    }
}