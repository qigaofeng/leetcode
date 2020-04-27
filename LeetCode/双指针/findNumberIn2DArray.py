from typing import List

def findNumberIn2DArray( matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    flag = 0
    print(n)
    for i in range(n):
        for j in range(n):
            #print(matrix[i][j])
            if matrix[i][j] == target:
                flag = 1
                break
    if flag == 1:
        return True
    else:
        return False
##########################################
    # i, j = len(matrix) - 1, 0
    # while i >= 0 and j < len(matrix[0]):
    #     if matrix[i][j] > target:
    #         i -= 1
    #     elif matrix[i][j] < target:
    #         j += 1
    #     else:
    #         return True
    # return False

if __name__ == "__main__":
    print(findNumberIn2DArray([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20))
