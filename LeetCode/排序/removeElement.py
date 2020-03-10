def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    numss = list(nums)
    for i in nums:
        #print(i)
        if i == val:
            numss.remove(i)
            #print(numss)
    #print(numss)
    #res = len(numss)
    return len(numss)

if __name__ == "__main__":
    print(removeElement([3,2,2,3],3))