def countCharacters(self, words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """
    ans = 0
    for w in words:
        for i in w:
            if w.count(i) > chars.count(i):
                break
        else:
            ans += len(w)
    return ans