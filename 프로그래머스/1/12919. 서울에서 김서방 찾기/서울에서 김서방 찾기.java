class Solution {
    public String solution(String[] seoul) {
        int kimLocation = 0;
        for (int i = 0 ; i < seoul.length; i++) {
            if (seoul[i].equals("Kim")) {
                kimLocation = i;
                break;
            }
        }
        String answer = "김서방은 " + kimLocation + "에 있다";
        return answer;
    }
}