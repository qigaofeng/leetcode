def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ########## 1
    # numss = list(set(nums))
    # list.sort(numss)
    # return len(numss)

    ###########  2
    # res = list(set(nums))
    # res.sort(key=nums.index)
    # print(res)
    # return len(res)

    ########## 3   前提是排序数组，所以可以这么比较
    i = 1
    while i <= len(nums) - 1:
        if nums[i] == nums[i - 1]:
            del nums[i]

        else:
            i += 1
    print(nums)

def removeDuplicates2(self, nums):    ###允许出现两次
    """
    :type nums: List[int]
    :rtype: int
    """
    k = 2
    nums_len = len(nums)
    while k < nums_len:
        if nums[k] == nums[k - 2]:
            del nums[k]
            nums_len -= 1
        else:
            k += 1
    return nums_len



if __name__ == "__main__":
    print(removeDuplicates(nums=[1, 2, 3,3,3]))

