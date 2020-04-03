def maxSatisfied(customers, grumpy, X):
    """
    :type customers: List[int]
    :type grumpy: List[int]
    :type X: int
    :rtype: int
    """
    n = len(grumpy)
    left = 0
    base_ans1 = 0
    max_windows_profit = 0
    current_windows_profit = 0
    for right in range(n):
        if grumpy[right] == 0:
            base_ans1 += customers[right]
            # print(base_ans1)
        current_windows_profit += customers[right] * grumpy[right]
        if right >= X:
            # if grumpy[left] == 0:
            #     base_ans1 -= customers[left]
            current_windows_profit -= customers[left] * grumpy[left]
            left += 1
        max_windows_profit = max(max_windows_profit, current_windows_profit)
    return base_ans1 + max_windows_profit

if __name__ == "__main__":
    print(maxSatisfied([1,0,1],[0,0,1],3))
