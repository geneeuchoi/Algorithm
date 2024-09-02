class Solution {
    public int[] solution(String[] wallpaper) {
        // wallpaper 일차원 배열을 이차원 배열로 변경
        int wallpaperLength = wallpaper.length;
        int elemLength = wallpaper[0].length();
        char[][] wallpaperArr = new char[wallpaperLength][elemLength];
        
        for(int i = 0; i < wallpaperLength; i++) {
            for(int j = 0; j < elemLength; j++) {
                wallpaperArr[i][j] = wallpaper[i].charAt(j);
            }
        }
        
        // 시작위치 가로 - #이 있는 첫번째로 있는 배열 인덱스 wallpaper[i]
        // 시작위치 세로 - #이 있는 제일 왼쪽에 있는 배열 인덱스 wallpaper[i][ㅓ]
        int started_width = 0;
        
        loop:
        for(int i = 0; i < wallpaperLength; i++) {
            for(int j = 0; j < elemLength; j++){
                if (wallpaperArr[i][j]=='#') {
                    started_width = i;
                    break loop;
                }
            }
        }
        
        int started_height = elemLength;
        for(int i = 0; i < wallpaperLength; i++) {
            for(int j = 0; j < elemLength; j++){
                if (wallpaperArr[i][j]=='#') {
                    started_height = started_height < j? started_height : j;
                }
            }
        }
        
        // 종료위치 가로 - #이 있는 마지막로 있는 배열 인덱스 wallpaper[i]
        // 종료위치 세로 - #이 있는 제일 오른쪽쪽에 있는 배열 인덱스 wallpaper[i][ㅓ]
        
        int finished_width = 0;
        
        for(int i = 0; i < wallpaperLength; i++) {
            for(int j = 0; j < elemLength; j++){
                if (wallpaperArr[i][j]=='#') {
                    finished_width = i;
                }
            }
        }
        
        int finished_height = 0;
        
        for(int i = 0; i < wallpaperLength; i++) {
            for(int j = 0; j < elemLength; j++){
                if (wallpaperArr[i][j]=='#') {
                    finished_height = finished_height > j? finished_height : j;
                }
            }
        }
        
        
        // return 배열 구하기
        int[] answer = {started_width, started_height, finished_width + 1,  finished_height + 1 };
        return answer;
    }
}