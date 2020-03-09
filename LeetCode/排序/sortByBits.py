from typing import List


def sortByBits(arr): #(  self, arr: List[int]) -> List[int]:
    #arr1 = list(arr)
    res = sorted(arr,key=lambda x:(bin(x).count('1'),x))
    return res
    #return sorted(arr, key=lambda x: (bin(x).count('1'), x))


if __name__ == "__main__":
    print(sortByBits([0,1,2,3,4,5,6,7,8]))