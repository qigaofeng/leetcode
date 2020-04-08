from collections import Counter


def shortestSeq(big, small):
    """
    :type big: List[int]
    :type small: List[int]
    :rtype: List[int]
    """
    left = 0
    n = len(big)
    ans = []
    min_lenth = n+1
    for right in range(n):
        #cur_set[big[right]] += 1
        while set(small).issubset(set(big[left:right])):
            print('1')
            print(big[left:right])
            if right - left + 1 < min_lenth:
                min_lenth = right - left + 1
                ans[:] = [left,right-1]
                print(ans)
            left += 1
    return ans

def shortestSeq1( big, small):
    from collections import Counter
    result = [float("inf"), float("inf")]
    left = 0
    n = len(big)
    small_set = set(small)
    cur_set = Counter()
    min_length = float("inf")
    for right in range(n):
        cur_set[big[right]] += 1
        while all(map(lambda x: x in cur_set and cur_set[x] > 0, small_set)):
            if right - left + 1 < min_length:
                min_length = right - left + 1
                result[:] = [left, right]
            elif right - left + 1 == min_length and left < result[0]:
                result[:] = [left, right]
            cur_set[big[left]] -= 1
            left += 1

    return result if result[0] != float("inf") else []

if __name__ == '__main__':
    print(shortestSeq([7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 2, 5, 8, 8, 9, 7],[1, 5, 9]))