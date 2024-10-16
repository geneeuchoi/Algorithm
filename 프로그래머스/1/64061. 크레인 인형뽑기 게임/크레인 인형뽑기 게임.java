import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        
        Deque<Integer> basket = new ArrayDeque<Integer>();
        int answer = 0;
        
        for(int moveIndex : moves) {
            for(int i = 0; i < board.length; i++) {
                if (board[i][moveIndex-1] != 0) {
                    basket.push(board[i][moveIndex-1]);
                    board[i][moveIndex-1] = 0;
                    break;
                }
            }
            
            if(basket.size() >= 2) {
                Integer tmp = 0;
                for(Integer elem : basket) {
                    if(elem == tmp) {
                        basket.pop();
                        basket.pop();
                        answer += 2;
                    }
                    tmp = elem;
                }
            }
        }
        
        return answer;
    }
}