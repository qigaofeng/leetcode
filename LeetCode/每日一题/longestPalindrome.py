import collections


def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    counter_s = collections.Counter(s)
    res, addtional = 0, 0
    for i in counter_s.values():
        if i % 2 == 0:
            res += i
        else:
            res += i - 1
            addtional = 1
    return res + addtional



if __name__ == "__main__":
    print(longestPalindrome("bb"))
