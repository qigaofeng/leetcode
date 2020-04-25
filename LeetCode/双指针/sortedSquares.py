def sortedSquares(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    res = []
    for i in A:
        k = i * i
        res.append(k)
    return sorted(res)


if __name__ == "__main__":
    print(sortedSquares([-4,-1,0,3,10]))