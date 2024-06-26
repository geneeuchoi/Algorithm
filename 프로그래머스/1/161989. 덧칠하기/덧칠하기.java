class Solution {
    public int solution(int n, int m, int[] section) {
        int roller = section[0];
        int cnt = 1;
        for(int i = 1; i < section.length; i++) {
            if(roller + m - 1 < section[i]) {
                cnt++;
                roller = section[i];
            }
        }
        return cnt;
    }
}



// import java.util.List;
// import java.util.ArrayList;

// class Solution {
//     public int solution(int n, int m, int[] section) {
        
//         List<Integer> painted = new ArrayList<>();
//         int count = 0;
        
//         for(int spot : section) {
//             for(int i = spot ; i < spot + m; i++) {
//                 if (!painted.contains(i)){
//                     painted.add(i);
//                     count += spot == i? 1 : 0;
//                     //painted에 spot이 들어갔다면 count를 추가해줘야 함.
                    
//                 } else{
//                     break;
//                 }
//             }
//         }
        
//         return count;
//     }
// }