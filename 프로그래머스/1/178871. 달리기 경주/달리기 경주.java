import java.util.HashMap;
import java.util.Map;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> playersMap = new HashMap<>();
        
        for(int i = 0; i < players.length; i++) {
            playersMap.put(players[i], i);
        }
        
        for(String calling : callings) {
            int calledPlayerRank = playersMap.get(calling);
            
            players[calledPlayerRank] = players[calledPlayerRank-1];
            players[calledPlayerRank-1] = calling;
            
            playersMap.put(players[calledPlayerRank-1], calledPlayerRank-1);
            playersMap.put(players[calledPlayerRank], calledPlayerRank);
        }

        return players;
    }
}