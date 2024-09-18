import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        // report 배열 중복 제거
        report = Arrays.stream(report).distinct().toArray(String[]::new);
        
        // 유저가 신고한 ID 이차원 어레이 리스트 생성
        ArrayList<String>[] banList = new ArrayList[id_list.length]; 

        // 각 인덱스의 ArrayList를 초기화
        for (int i = 0; i < id_list.length; i++) {
            banList[i] = new ArrayList<String>();
        }
        
        // 각 아이디 별 신고된 횟수를 구하기 위한 맵 생성
        HashMap<String, Integer> banRoundMap = new HashMap<String, Integer>();
        
        // 맵 초기화
        for(String id: id_list) {
            banRoundMap.put(id, 0);
        }
        
        for(String reportElem : report) {
            String[] reportArr = new String[2];
            reportArr = reportElem.split(" ");
            for(int i = 0; i < id_list.length; i++) {
                // 유저 아이디 인덱스에 맞춰 유저가 신고한 ID 추가
                if(id_list[i].equals(reportArr[0])) {
                    banList[i].add(reportArr[1]);
                    // 신고된 아이디마다 맵 횟수 증가
                    int bannedRound = banRoundMap.get(reportArr[1]) + 1;
                    banRoundMap.put(reportArr[1], bannedRound);
                }
            }
        }
        
        // banList[i]의 리스트를 돌면서, 그 각각의 값들이 k이상이면 answer[i] += 1;
        // id_list[i]>k이면 answer[i] += 1;
        int[] answer = new int[id_list.length];
        
        for(int i = 0; i < banList.length; i++) {
            for(int j = 0; j < banList[i].size(); j++) {
                if (banRoundMap.get(banList[i].get(j)) >= k) {
                    answer[i] += 1;
                }
            }
        }
        return answer;
    }
}
