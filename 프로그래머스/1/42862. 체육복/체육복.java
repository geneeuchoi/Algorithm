import java.util.Arrays;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        //초기 세팅
        int[] clothes = new int[n];
        
        for(int i = 0; i < clothes.length; i++) {
            clothes[i] = 1;
        }
        
        for(int reserveNum : reserve) {
            clothes[reserveNum-1] += 1;
        }
        
        for(int lostNum : lost) {
            clothes[lostNum-1] -= 1;
        }
        
        for(int i = 0; i < n; i++) {
            
            if(i > 0 && clothes[i] == 0 && clothes[i-1] == 2) {
                clothes[i] += 1;
                clothes[i-1] -=1;
            }
            
            if(i < n-1 && clothes[i] == 0 && clothes[i+1] == 2) {
                clothes[i] += 1;
                clothes[i+1] -=1;
            }
            
        }
        
        //체육수업을 들을 수 있는 학생 수 카운트
        int cnt = 0;
        
        for(int clothe : clothes) {
            if(clothe != 0) cnt += 1;
        }
        
        return cnt;
    }
}