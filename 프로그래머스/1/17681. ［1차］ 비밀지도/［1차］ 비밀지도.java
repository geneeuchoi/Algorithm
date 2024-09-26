class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] strArr1 = exchangeArr(arr1, n);
        String[] strArr2 = exchangeArr(arr2, n);
        
        String[] answer = new String[n];
        
        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                if (strArr1[i].charAt(j) == '0' && strArr2[i].charAt(j) == '0') {
                    sb.append(" ");
                } else {
                    sb.append("#");
                }
            }
            answer[i] = sb.toString();
        }

        return answer;
    }
    
    public String[] exchangeArr(int[] arr, int mapLength) {
        String[] strArr = new String[arr.length];
        for (int i = 0; i < arr.length; i++) {
            strArr[i] = exchangeValue(arr[i], mapLength);
        }
        return strArr;
    }
    
    public String exchangeValue(int num, int mapLength) {
        // 정수를 2진수 문자열로 변환
        String binaryString = Integer.toBinaryString(num);
        
        // mapLength보다 짧을 경우 앞에 '0'을 추가
        while (binaryString.length() < mapLength) {
            binaryString = "0" + binaryString;
        }
        
        return binaryString;
    }
}
