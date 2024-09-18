import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String s) {
        // 공백마다 나눈 후에, int형으로 어레이 리스트에 추가한다.
        // 어레이 리스트를 돌면서 최댓값 최솟값을 찾아 answer 배열에 추가한다.
        List<Integer> sList = Arrays.stream(s.split(" "))
                                .map(Integer::parseInt)
                                .collect(Collectors.toList());
        
        StringBuilder sb = new StringBuilder();
        String max = Collections.max(sList).toString();
        String min = Collections.min(sList).toString();
        
        return sb.append(min).append(" ").append(max).toString();
    }
}