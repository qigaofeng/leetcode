def minIncrementForUnique(A):
    """
    :type A: List[int]
    :rtype: int
    """
    A.sort()
    print(A)
    move = 0
    for i in range(1, len(A)):
        if A[i] <= A[i - 1]:
            move += A[i - 1] - A[i] + 1
            A[i] = A[i - 1] + 1
    return move

if __name__ == '__main__':
    print(minIncrementForUnique([3,2,1,2,1,7]))