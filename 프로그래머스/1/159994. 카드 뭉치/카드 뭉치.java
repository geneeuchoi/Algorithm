class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        int i = 0;
        int j = 0;
        for(String elem : goal) {
            int beforeI = i;
            int beforeJ = j;
            if (i < cards1.length && cards1[i].equals(elem)) {
                i++;
            }
            if (j < cards2.length && cards2[j].equals(elem)) {
                j++;
            }
            if (beforeI == i && beforeJ == j) {
                return "No";
            }
        }
        return "Yes";
    }
}