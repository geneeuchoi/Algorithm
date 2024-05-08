class Solution {
    public int[] solution(long n) {
        //n의 길이 확인하기
        long nSize = n;
        int cnt = 0;
        while (nSize >0) {
            cnt++;
            nSize /= 10;
        }
        
        int[] answer = new int[cnt];
        
        for (int i = 0; i < cnt; i++) {
            answer[i] = (int)(n % 10);
            n /= 10;
        }
        return answer;
    }
}
