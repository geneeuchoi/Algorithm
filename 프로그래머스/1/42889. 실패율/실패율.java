import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        
        int[] gamers = new int[N+1];
        
        for(int i = 0; i < stages.length; i++) {
            gamers[stages[i]-1] += 1;
        }
        
        float[] failRate = new float[N];
        int totalGamers = stages.length;
        for(int i = 0; i < gamers.length-1; i++) {
            failRate[i] = (float)gamers[i] / totalGamers;
            totalGamers -= gamers[i];
        }
        
        List<int[]> stageFailList = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            stageFailList.add(new int[]{i + 1, failRate[i]});
        }
        
        Collections.sort(stageFailList, (a, b) -> {
            if (b[1] == a[1]) {
                return Integer.compare(a[0], b[0]);
            } else {
                return Float.compare(b[1], a[1]);
            }
        });
        
        // 정렬된 스테이지 번호만 배열로 추출
        int[] answer = new int[N];
        for (int i = 0; i < N; i++) {
            answer[i] = stageFailList.get(i)[0];
        }
        
        return answer;
    }
}