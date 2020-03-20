def getLeastNumbers(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: List[int]
    """
    list.sort(arr)
    return arr[:k]