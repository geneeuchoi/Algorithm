import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
        Stack<Integer> stack = new Stack<>();
        int answer = 0;
        int[] pattern = {1, 2, 3, 1};
        int patternLength = pattern.length;

        for (int material : ingredient) {
            stack.push(material);

            // 스택의 크기가 패턴의 길이 이상일 때 패턴을 검사
            if (stack.size() >= patternLength) {
                boolean isPattern = true;
                for (int i = 0; i < patternLength; i++) {
                    if (stack.get(stack.size() - patternLength + i) != pattern[i]) {
                        isPattern = false;
                        break;
                    }
                }
                // 패턴이 맞다면 패턴 길이만큼 스택에서 제거
                if (isPattern) {
                    for (int i = 0; i < patternLength; i++) {
                        stack.pop();
                    }
                    answer++;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] ingredient = {1, 2, 3, 1, 2, 3, 1, 1, 2, 3, 1};
        System.out.println(sol.solution(ingredient)); // 출력 예시: 3
    }
}
