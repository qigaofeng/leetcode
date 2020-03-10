def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    # 使用了额外的数组空间
    numss = list(nums)
    for i in nums:
        #print(i)
        if i == val:
            numss.remove(i)
            #print(numss)
    #print(numss)
    #res = len(numss)
    return len(numss)

def removeElement(self, nums: List[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)



if __name__ == "__main__":
    print(removeElement([3,2,2,3],3))