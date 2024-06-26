class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int minCnt = 0;
        int maxCnt = 0;
        int zeroCnt = 0;
        
        for(int num : lottos) {
            for (int i = 0; i < win_nums.length; i++) {
                minCnt += num == win_nums[i]? 1 : 0;
            }
            if(num == 0) zeroCnt +=1;
        }
        
        
        
        maxCnt = minCnt + zeroCnt;
        System.out.println(minCnt);
        System.out.println(zeroCnt);
        System.out.println(maxCnt);
        
        
        int[] answer = new int[2];
        answer[0] = place(maxCnt);
        answer[1] = place(minCnt);
        return answer;
    }
    
    public int place(int cnt) {
        int grade = 0;
        if(cnt == 6) grade = 1;
        else if(cnt == 5) grade = 2;
        else if(cnt == 4) grade = 3;
        else if(cnt == 3) grade = 4;
        else if(cnt == 2) grade = 5;
        else grade = 6;
        
        return grade;
    }
}