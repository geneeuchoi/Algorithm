class Solution {
    int[] zeroAndOne = new int[2];
    
    public int[] solution(int[][] arr) {
        splitedSum(arr, 0, 0, arr.length);
        
        return zeroAndOne;
    }
    
    public void splitedSum(int[][] arr, int row, int column, int size) {
        if(isAllZeroOrOne(arr, row, column, size)) {
            if(arr[row][column] == 0) zeroAndOne[0]++;
            if(arr[row][column] == 1) zeroAndOne[1]++;
            return;
        } 
        
        int newSize = size/2;
        
        splitedSum(arr, row, column, newSize);
        splitedSum(arr, row, column+newSize, newSize);
        splitedSum(arr, row+newSize, column, newSize);
        splitedSum(arr, row+newSize, column+newSize, newSize);
        
    }
    
    public boolean isAllZeroOrOne(int[][] arr, int row, int column, int size) {
        
        int value = arr[row][column];
        for (int i = row; i < row + size; i++) {
            for (int j = column; j < column + size; j++) {
                if (arr[i][j] != value) {
                    return false;
                }
            }
        }
        return true;
    }
}