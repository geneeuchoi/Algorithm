class Solution {
    public int[] solution(String[] park, String[] routes) {
        // result = {a, b}라고 할때
        int[] result = new int[2];
        
        // 초기 설정은 park에서 s가 있는 {배열의 인덱스, 해당 인덱스 내의 charAt()}
        for(int i = 0 ; i < park.length; i++) {
            if(park[i].contains("S")) {
                result[0] = i;
                result[1] = park[i].indexOf("S");
            }
        }
        
        // routes가 e일 때에는 {a, b+charAt(2)}
        // w일때에는 {a, b-charAt(2)}
        // s일 때에는 {a + charAt(2), b}
        // n일 때에는 {a - charAt(2), b}
        
        int tmp = 0;
        for(String route : routes) {
            switch (route.charAt(0)) {
                case 'E':
                    // 동쪽으로 이동
                    tmp = result[1] + Character.getNumericValue(route.charAt(2));
                    // 조건 1: 길이가 맞는가?
                    if(tmp < park[0].length() && tmp >= 0) {
                        // 조건 2: 가는 길에 x가 있는가?
                        boolean flag = true;
                        for(int i = result[1]; i <= tmp; i++) {
                            if(park[result[0]].charAt(i) == 'X') {
                                flag = false;
                            }
                        }
                        if(flag) result[1] = tmp;
                    }
                    break;
                case 'W':
                    tmp = result[1] - Character.getNumericValue(route.charAt(2));
                    if(tmp < park[0].length() && tmp >= 0) {
                        boolean flag = true;
                        for(int i = result[1]; i >= tmp; i--) {
                            if(park[result[0]].charAt(i) == 'X') {
                                flag = false;
                            }
                        }
                        if(flag) result[1] = tmp;
                    }
                    break;
                case 'S':
                    tmp = result[0] + Character.getNumericValue(route.charAt(2));
                    if(tmp < park.length && tmp >= 0) {
                        boolean flag = true;
                        for(int i = result[0]; i <= tmp; i++) {
                            if(park[i].charAt(result[1]) == 'X') {
                                flag = false;
                            }
                        }
                        if(flag) result[0] = tmp;
                    }
                    break;
                case 'N':
                    tmp = result[0] - Character.getNumericValue(route.charAt(2));
                    if(tmp < park.length && tmp >= 0) {
                        boolean flag = true;
                        for(int i = result[0]; i >= tmp; i--) {
                            if(park[i].charAt(result[1]) == 'X') {
                                flag = false;
                            }
                        }
                        if(flag) result[0] = tmp;
                    }
                    break;
            }
            System.out.println(route);
            System.out.println(result[0]);
            System.out.println(result[1]);
        }
        return result;
        
    }
}