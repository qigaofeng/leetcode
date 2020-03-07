
def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    list = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                list.append(nums1[i])
    res = {}.fromkeys(list).keys()
    return res
    #return list(set(nums1) & set(nums2))   直接


if __name__ == "__main__":
    print(intersection(nums1=[1, 2, 2, 1], nums2=[2, 1]))