class Solution {
    public String solution(String rny_string) {
        if (rny_string.contains("m")) rny_string = rny_string.replace("m", "rn");
        return rny_string;
    }
}