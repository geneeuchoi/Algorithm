class Solution {
    public int solution(int[] nums) {
        int result = 0;
        int num;
        
        for(int i = 0; i < nums.length-2; i++) {
            for(int j = i + 1; j < nums.length-1; j++) {
                for(int k = j + 1; k < nums.length; k++) {
                    num = 0;
                    num = nums[i] + nums[j] + nums[k];
                    
                    if(!isSosu(num)) result += 1;
                    
                }
            }
        }
        
        return result;
    }
    
    public boolean isSosu(int num) {
        for(int l = 2; l < num; l++) {
            if (num % l == 0) {
                return true;
            }
        }
        return false;
    }
}