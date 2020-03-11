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

    ########## 3
    i = 1
    while i <= len(nums) - 1:
        if nums[i] == nums[i - 1]:
            del nums[i]
        else:
            i += 1
    print(nums)




if __name__ == "__main__":
    print(removeDuplicates(nums=[5, 3, 3,1,3]))

