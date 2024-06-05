import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(int[][] sizes) {
        
        for(int i = 0; i < sizes.length; i++) {
            if(sizes[i][1] >= sizes[i][0]) {
                int tmp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = tmp;
            }
        }
        
        int lengthMax0 = 0;
        int lengthMax1 = 0;
        
        for (int i = 0; i < sizes.length; i++) {
            lengthMax0 = sizes[i][0] >= lengthMax0? sizes[i][0] : lengthMax0;
            lengthMax1 = sizes[i][1] >= lengthMax1? sizes[i][1] : lengthMax1;
        }
        
        return lengthMax0 * lengthMax1;
    }
}