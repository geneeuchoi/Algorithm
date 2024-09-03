import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        // terms를 맵으로 바꾸기
        HashMap<Character, Integer> termsMap = new HashMap<>();

        for (String term : terms) {
            termsMap.put(term.charAt(0), Integer.parseInt(term.substring(2)));
        }

        int i = 1;
        List<Integer> answerList = new ArrayList<>();

        // 오늘 날짜를 연, 월, 일로 분리하여 숫자로 저장
        int todayYear = Integer.parseInt(today.substring(0, 4));
        int todayMonth = Integer.parseInt(today.substring(5, 7));
        int todayDay = Integer.parseInt(today.substring(8, 10));

        // 가입한 날로부터 지난 날짜 구하기
        for (String privacie : privacies) {
            int passedDays = termsMap.get(privacie.charAt(11)) * 28;
            int startDay = Integer.parseInt(privacie.substring(8, 10));
            int startMonth = Integer.parseInt(privacie.substring(5, 7));
            int startYear = Integer.parseInt(privacie.substring(0, 4));

            // plusedDay와 plusedMonth 계산
            int plusedDay = startDay + passedDays - 1;
            int expiredDay = (plusedDay % 28 == 0) ? 28 : plusedDay % 28;
            int plusedMonth = startMonth + (plusedDay - 1) / 28;

            // expiredMonth와 expiredYear 계산
            int expiredYear = startYear + (plusedMonth - 1) / 12;
            int expiredMonth = (plusedMonth - 1) % 12 + 1;

            // 만약 expiredMonth가 0이면, 12월로 조정하고 연도를 하나 줄임
            if (expiredMonth == 0) {
                expiredMonth = 12;
                expiredYear -= 1;
            }

            // 오늘 날짜와 비교 후 만료된 경우 answerList에 추가
            if (todayYear > expiredYear ||
                    (todayYear == expiredYear && todayMonth > expiredMonth) ||
                    (todayYear == expiredYear && todayMonth == expiredMonth && todayDay > expiredDay)) {
                answerList.add(i);
            }

            i++;
        }

        // answer을 오름차순으로 정렬 후 return
        int[] answer = new int[answerList.size()];
        for (int j = 0; j < answerList.size(); j++) {
            answer[j] = answerList.get(j);
        }

        return answer;
    }
}
