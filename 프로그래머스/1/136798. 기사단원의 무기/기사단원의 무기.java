class Solution {
    public int solution(int number, int limit, int power) {
        
        int cnt;
        int weight = 0;
        
        for(int i = 1 ; i < number+1 ; i++) {
            cnt = 0;
            for(int j = 1; j * j <= i; j++) {
                if(j * j == i) cnt++;
                else if(i % j == 0) cnt+=2;
            }
            
            
            weight += weightCal(cnt, limit, power);
        }
        

        return weight;
    }
    
    
    public int weightCal(int cnt, int limit, int power) {
        int answer = 0;
        if(cnt<=limit) {
                answer += cnt;
            } else {
                answer += power;
            }
        return answer;
    }
}