import java.util.*;

class Solution {
    public String solution(String X, String Y) {
        int[] xCount = new int[10];
        int[] yCount = new int[10];
        
        // X와 Y의 각 문자의 빈도를 카운팅
        for (char c : X.toCharArray()) {
            xCount[c - '0']++;
        }
        for (char c : Y.toCharArray()) {
            yCount[c - '0']++;
        }
        
        List<Character> same = new ArrayList<>();
        
        // 교집합 구하기
        for (int i = 0; i < 10; i++) {
            int minCount = Math.min(xCount[i], yCount[i]);
            for (int j = 0; j < minCount; j++) {
                same.add((char) (i + '0'));
            }
        }
        
        // 내림차순 정렬
        same.sort(Comparator.reverseOrder());
        
        if (same.isEmpty()) return "-1";
        else if (isAllZero(same)) return "0";
        else return builder(same);
    }
    
    public boolean isAllZero(List<Character> same) {
        for (char elem : same) {
            if (elem != '0') {
                return false;
            }
        }
        return true;
    }
    
    public String builder(List<Character> same) {
        StringBuilder sb = new StringBuilder();
        
        for (char elem : same) {
            sb.append(elem);
        }
        
        return sb.toString();
    }
}
