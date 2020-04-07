def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    left = 0
    ans = 1
    current = 0
    ss = list(s)
    n = len(ss)
    if n == 0:
        return 0
    for right in range(1, n):
        if ss[right] not in ss[left:right]:
            ans = max(ans, right - left + 1)
        else:
            while ss[right] in ss[left:right]:
                left += 1
    return ans

if __name__ == "__main__":
    print(lengthOfLongestSubstring("asbdsa"))