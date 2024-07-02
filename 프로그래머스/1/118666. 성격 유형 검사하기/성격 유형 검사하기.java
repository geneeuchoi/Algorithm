import java.util.*;
class Solution {
    public String solution(String[] survey, int[] choices) {
        //초기 설정
        Map<Character, Integer> userChoice = new HashMap<>();
        
        userChoice.put('R', 0);
        userChoice.put('T', 0);
        userChoice.put('C', 0);
        userChoice.put('F', 0);
        userChoice.put('J', 0);
        userChoice.put('M', 0);
        userChoice.put('A', 0);
        userChoice.put('N', 0);
        
        Map<Integer, Integer> score = new HashMap<>();
        
        score.put(1, 3);
        score.put(2, 2);
        score.put(3, 1);
        score.put(4, 0);
        score.put(5, 1);
        score.put(6, 2);
        score.put(7, 3);
        
        //유저 선택에 따른 점수 합산하기
        Character type;
        
        for(int i = 0; i < survey.length; i++) {
            if(choices[i]>= 5) {
                type = survey[i].charAt(1);
                userChoice.put(type, userChoice.get(type) + score.get(choices[i]));
                
            } else if(choices[i] < 4) {
                type = survey[i].charAt(0);
                userChoice.put(type, userChoice.get(type) + score.get(choices[i]));        
            }
            
        }
        
        //점수에 따라 성격 검사 결과 변환
        StringBuilder sb = new StringBuilder();
        
        if (userChoice.get('R') >= userChoice.get('T')) sb.append('R');
        else sb.append('T');
        
        if (userChoice.get('C') >= userChoice.get('F')) sb.append('C');
        else sb.append('F');
        
        if (userChoice.get('J') >= userChoice.get('M')) sb.append('J');
        else sb.append('M');
        
        if (userChoice.get('A') >= userChoice.get('N')) sb.append('A');
        else sb.append('N');
        
        
        return sb.toString();
    }
}