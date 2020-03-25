def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    haystack_switch = list(haystack)
    needle_switch = list(needle)
    m, n = len(haystack_switch), len(needle_switch)
    if len(needle_switch) == 0:
        return 0
    for start in range(m - n + 1):
        if haystack_switch[start:start + n ] == needle_switch[:]:
            return start

    return -1


def strStr1(haystack, needle):
    L, n = len(needle), len(haystack)

    for start in range(n - L + 1):
        if haystack[start: start + L] == needle:
            return start
    return -1


if __name__ == "__main__":
    print(strStr(haystack="hello", needle="ll"))
    print(strStr1(haystack="hello", needle="ll"))
