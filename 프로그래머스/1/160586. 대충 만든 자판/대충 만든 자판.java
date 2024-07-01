import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        HashMap<Character, Integer> map = new HashMap<>();
        
        for(String key : keymap) {
            
            for(int i = 0; i < key.length(); i++) {
                
                if (map.containsKey(key.charAt(i))) {
                
                    Integer currentCnt = map.get(key.charAt(i));
                    
                    if(currentCnt> i+1) {
                      map.put(key.charAt(i), i+1);   
                    }
                } else {
                    map.put(key.charAt(i), i+1);
                } 
            }
        }
        
        System.out.println(map);
        
        for(int t = 0; t < targets.length; t++) {
            String target = targets[t];
            int min = 0;
            for(int k = 0; k < target.length(); k++) {
                if(!map.containsKey(target.charAt(k))) {
                    min = -1;
                    break;
                } else {
                    min += map.get(target.charAt(k));
                }
            }
            answer[t] = min;
        }
        
        
        
        return answer;
    }
}