class Solution {
    public int solution(int[][] dots) {
        
        int width = dots[0][0];
        int height = dots[0][1];
        
        width = lengthCal(dots, width, 0);
        height = lengthCal(dots, height, 1);
        
        return width * height;
    }
    
    public int lengthCal(int[][] dots, int height, int n) {
        for(int[] arr : dots) {
            if(height != arr[n]) {
                if (height > arr[n]) height = height -arr[n];
                else height = arr[n] - height;
                break;
            }
        }
        return height;
    }
}