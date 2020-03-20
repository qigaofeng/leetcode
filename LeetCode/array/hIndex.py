def hIndex( citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    if len(citations) <= 0 or any(citations) == False:  #citations 都为0
        return 0
    dict = {}
    value = 0
    for i in range(1, len(citations) + 1):
        for j in citations:
            if j >= i:
                value += 1
        dict[i] = value
        value = 0
    for k, v in dict.items():
        if k == v:
            res = v
    return res


if __name__ == '__main__':
    print(hIndex([3,0,6,1,5]))
