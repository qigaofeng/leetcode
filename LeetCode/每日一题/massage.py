def massage(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0:
        return 0
    dp0, dp1 = 0, nums[0]
    for i in range(1, n):
        temp_dp0 = max(dp0, dp1)
        temp_dp1 = dp0 + nums[i]
        dp0 = temp_dp0
        dp1 = temp_dp1
    return max(dp0, dp1)