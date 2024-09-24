import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        List<Integer> arrList = new ArrayList<>();
        
        int tmp = arr[0];
        arrList.add(tmp);
        
        for(int i = 1; i < arr.length; i++) {
            if (tmp != arr[i]) {
                arrList.add(arr[i]);
                tmp = arr[i];
            }
        }
        
        int[] answer = new int[arrList.size()];
        for(int i = 0; i < answer.length; i++) {
            answer[i] = arrList.get(i);
        }
        
        return answer;
    }
}