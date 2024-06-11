import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int answerIndex = 0;
        
        //배열 자르기
        for (int[] elem : commands) {            
            int[] bowl = new int[elem[1]-elem[0]+1];
            int bowlIndex = 0;
            
            //i~j의 값 꺼내기
            for (int i = elem[0]-1; i <= elem[1]-1; i++) {
                bowl[bowlIndex] = array[i];
                bowlIndex++;
            }
            //정렬한 리스트에서 k가져오기
            Arrays.sort(bowl);
            int k = bowl[elem[2]-1];
            
            //k를 배열에 담기
            answer[answerIndex] = k;
            answerIndex++;
        }
        
        return answer;
    }
}