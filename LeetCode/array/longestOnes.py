def longestOnes(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    n = len(A)
    left = 0
    count_0 = 0
    ans = 0
    for right in range(n):
        if A[right] == 0:
            count_0 += 1
        while count_0 > K:
            if A[left] == 0:
                count_0 -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

if __name__ == "__main__":
    print(longestOnes([1,0,1,1,1],1))