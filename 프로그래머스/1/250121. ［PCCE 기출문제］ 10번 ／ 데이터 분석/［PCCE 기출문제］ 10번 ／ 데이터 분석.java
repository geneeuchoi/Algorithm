import java.util.*;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        
        List<Integer> indexList= new ArrayList<>();
        
        for(int i = 0; i < data.length; i++) {
            switch(ext) {
                case "code":
                    if (data[i][0] < val_ext) indexList.add(i);
                    break;
                case "date":
                    if (data[i][1] < val_ext) indexList.add(i);
                    break;
                case "maximum":
                    if (data[i][2] < val_ext) indexList.add(i);
                    break;
                case "remain":
                    if (data[i][3] < val_ext) indexList.add(i);
                    break;
            }
        }
        
        int[] indexArr = indexList.stream().mapToInt(Integer::intValue).toArray();
        int[] sortByArr= new int[indexList.size()];
        int sortByArrIndex = 0;
        
        // String sort_by에 해당하는 값들을 오름차순으로 정렬한다.
        for(int index : indexArr) {
            switch(sort_by) {
                case "code":
                    sortByArr[sortByArrIndex] = data[index][0];
                    sortByArrIndex++;
                    break;
                case "date":
                    sortByArr[sortByArrIndex] = data[index][1];
                    sortByArrIndex++;
                    break;
                case "maximum":
                    sortByArr[sortByArrIndex] = data[index][2];
                    sortByArrIndex++;
                    break;
                case "remain":
                    sortByArr[sortByArrIndex] = data[index][3];
                    sortByArrIndex++;
                    break;
            }
        }
        
        Arrays.sort(sortByArr);
        int[][] answer = new int[indexList.size()][4];
        int answerIndex = 0;
        for(int sortByArrElem : sortByArr) {
            switch(sort_by) {
                case "code":
                    for(int i = 0; i < data.length; i++) {
                        if(data[i][0] == sortByArrElem) {
                            answer[answerIndex][0] = data[i][0];
                            answer[answerIndex][1] = data[i][1];
                            answer[answerIndex][2] = data[i][2];
                            answer[answerIndex][3] = data[i][3];
                            answerIndex++;
                        }
                    }
                    break;
                case "date":
                    for(int i = 0; i < data.length; i++) {
                        if(data[i][1] == sortByArrElem) {
                            answer[answerIndex][0] = data[i][0];
                            answer[answerIndex][1] = data[i][1];
                            answer[answerIndex][2] = data[i][2];
                            answer[answerIndex][3] = data[i][3];
                            answerIndex++;
                        }
                    }
                    break;
                case "maximum":
                    for(int i = 0; i < data.length; i++) {
                        if(data[i][2] == sortByArrElem) {
                            answer[answerIndex][0] = data[i][0];
                            answer[answerIndex][1] = data[i][1];
                            answer[answerIndex][2] = data[i][2];
                            answer[answerIndex][3] = data[i][3];
                            answerIndex++;
                        }
                    }
                    break;
                case "remain":
                    for(int i = 0; i < data.length; i++) {
                        if(data[i][3] == sortByArrElem) {
                            answer[answerIndex][0] = data[i][0];
                            answer[answerIndex][1] = data[i][1];
                            answer[answerIndex][2] = data[i][2];
                            answer[answerIndex][3] = data[i][3];
                            answerIndex++;
                        }
                    }
                    break;
            }
        }
        
        return answer;
    }
}