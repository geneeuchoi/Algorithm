class Solution {
    public int solution(int[][] triangle) {
        // i -> i, i+1 둘 중 큰 것 찾아서 더하고 값 바꾸기
        //triangle[0][0]이 정답이다.
        
        for(int i = triangle.length - 1; i > 0; i--) {
            for(int k = 0; k < triangle[i].length-1; k++) {
                triangle[i-1][k] += (triangle[i][k] >= triangle[i][k+1])?
                    triangle[i][k] : triangle[i][k+1];
            }
        }
        
        return triangle[0][0];
    }
}
