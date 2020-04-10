def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    from collections import defaultdict
    # ss = list(s)
    left = 0
    ans = 0
    maxFreq = 0
    freqDict = defaultdict(int)
    for right in range(len(s)):
        right_char = s[right]
        freqDict[right_char] += 1
        maxFreq = max(maxFreq, freqDict[right_char])
        if (right - left + 1 - maxFreq) > k:
            left_char = s[left]
            left += 1
            freqDict[left_char] -= 1
        ans = max(ans, right - left + 1)
    return ans


def characterReplacement1(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    from collections import defaultdict
    # 动态滑动窗口
    maxLen, windowStart, maxFreq = 0, 0, 0
    # 统计出现频率
    freqDict = defaultdict(int)
    for windowEnd in range(len(s)):
        rightChar = s[windowEnd]
        freqDict[rightChar] += 1
        # 保存历史出现的最大频率
        maxFreq = max(freqDict[rightChar], maxFreq)
        # 缩小滑动窗口
        if (windowEnd - windowStart + 1 - maxFreq) > k:
            leftChar = s[windowStart]
            windowStart += 1
            freqDict[leftChar] -= 1
        maxLen = max(maxLen, windowEnd - windowStart + 1)
    return maxLen


if __name__ == "__main__":
    print(characterReplacement(s="ABBA", k=2))
