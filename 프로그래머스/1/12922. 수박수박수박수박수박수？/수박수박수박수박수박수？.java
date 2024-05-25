class Solution {
    public String solution(int n) {
        StringBuilder sb = new StringBuilder(); 
        for(int i = 0 ; i < n; i++) {
          switch(i % 2) {
              case 0 -> sb.append("수");
              case 1 -> sb.append("박");
            }
        }
    return sb.toString();
    }
}