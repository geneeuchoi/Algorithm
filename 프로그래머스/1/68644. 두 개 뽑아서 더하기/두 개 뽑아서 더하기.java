import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;

class Solution {
    public Integer[] solution(int[] numbers) {
        Set<Integer> set = new HashSet<>();
        
        for(int i = 0; i < numbers.length; i++) {
            for(int j = i+1; j < numbers.length; j++) {
                set.add(numbers[i] + numbers[j]);
            }
        }
        
        Integer[] answer = set.toArray(new Integer[0]);
        Arrays.sort(answer);
        return answer;
    }
}