def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    nums_len = len(nums)
    for i in range(k):
        previous = nums[nums_len - 1]
        for j in range(nums_len):
            temp = nums[j]
            nums[j] = previous
            previous = temp
    return nums

def rotate2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    nums_len = len(nums)
    nums[:] = nums[nums_len - k:] + nums[:nums_len - k]
    return nums

if __name__ == "__main__":
    print(rotate(nums=[1,2,3,4,5], k=2))