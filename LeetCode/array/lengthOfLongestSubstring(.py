def lengthOfLongestSubstring(s):
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


def lengthOfLongestSubstring1(s):
    """
    :type s: str
    :rtype: int
    """
    from collections import defaultdict
    ans, left = 0, 0
    freq_dict = defaultdict(int)
    for right in range(len(s)):
        right_char = s[right]
        freq_dict[right_char] += 1
        # print(freq_dict[right_char])
        while freq_dict[right_char] > 1:
            leftChar = s[left]
            left += 1
            freq_dict[leftChar] -= 1
        ans = max(right - left + 1, ans)
    return ans


if __name__ == "__main__":
    print(lengthOfLongestSubstring1("pwwkew"))
