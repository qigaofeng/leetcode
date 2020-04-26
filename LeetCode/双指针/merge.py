from typing import List


def merge(A: List[int], m: int, B: List[int], n: int) -> List[int]:
    """
    Do not return anything, modify A in-place instead.
    """
    # len_B = len(B)
    j = 0

    # A[m:] = B
    # A.sort()
    for i in range(n, m + n):
        # j = 0
        A[i] = B[j]
        j += 1
        # print("1")
    print(A)
    ans = sorted(A)
    return ans


if __name__ == "__main__":
    print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    # print(sorted([2, 1, 5, 4, 2]))
    # A = [2, 1, 5, 4, 2]
    # B = sorted(A)
    # print(B)
