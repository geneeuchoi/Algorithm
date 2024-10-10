class Solution {
    public int[] solution(int n) {
        int[][] triangle = new int[n][n];
        int[] answer = new int[n * (n + 1) / 2];
        
        int value = 1;
        int x = -1, y = 0; // 시작 위치 (x를 -1로 시작해서 첫 이동이 아래로 가도록 함)
        
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (i % 3 == 0) { // 아래로 이동
                    x++;
                } else if (i % 3 == 1) { // 오른쪽으로 이동
                    y++;
                } else if (i % 3 == 2) { // 대각선 위로 이동
                    x--;
                    y--;
                }
                triangle[x][y] = value++;
            }
        }

        // 삼각형 배열에서 값 추출해 1차원 배열로
        int index = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                answer[index++] = triangle[i][j];
            }
        }
        
        return answer;
    }
}
