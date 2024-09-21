class Solution {
    public int[] solution(int brown, int yellow) {
        int tiles = brown + yellow;
        int width = 0; // 가로
        int height = 0; // 세로
        
        int[] answer = new int[2];
        for(int i = 3; i <= tiles/2; i++) {
            if (tiles % i == 0 && tiles / i >= i) {
                width = tiles / i;
                height = i;
                if((width * 2 + height * 2 -4) == brown && 
                   tiles - (width * 2 + height * 2 -4) == yellow) {
                    answer[0] = width;
                    answer[1] = height;
                    break;
                }
            }
        }
        
        return answer;
    }
}