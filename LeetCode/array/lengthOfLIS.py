def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # start = 0 # 滑动窗口的左边界
    end = 1  # 滑动窗口的右边界
    # sum = 0 # 滑动窗口中数字的和
    length = 1
    res = []
    while end != len(nums):
        if nums[end] > nums[end - 1]:
            # 右边界向右移动
            end += 1
            length += 1
        else:
            res.append(length)
            length = 1
            # 左边界向右移动
            end += 1
    return max(res)

if __name__ == "__main__":
    print(lengthOfLIS([10,9,2,5,3,7,101,18]))