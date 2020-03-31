def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    n = len(nums)
    if n == 0:
        return []
    left = 0
    right = k
    res = []
    while right <= n:
        ans = max(nums[left:right])
        # print(nums[left:right])
        res.append(ans)
        left += 1
        right += 1
    return res

if __name__ == "__main__":
    print(maxSlidingWindow([1,123,4,2],3))