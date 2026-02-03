def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        for n in range(len(arr1[0])):
            for j in range(len(arr2[0])):
                answer[i][j] += arr1[i][n] * arr2[n][j]
    return answer