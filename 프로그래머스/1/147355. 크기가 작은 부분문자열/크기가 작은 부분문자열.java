class Solution {
    public int solution(String t, String p) {
        int cnt = 0;
        for (int i = 0; i < t.length() - p.length() + 1; i++){
            String str = t.substring(i,i + p.length());
            Long pInt = Long.parseLong(p);
            Long strInt = Long.parseLong(str);
            cnt += (strInt <= pInt)? 1 : 0;
        }        
        return cnt;
    }
}