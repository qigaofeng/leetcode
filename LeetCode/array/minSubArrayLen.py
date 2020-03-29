def minSubArrayLen(s,nums):
    l = total = 0
    ans = len(nums) + 1
    for r in range(len(nums)):
        total += nums[r]
        while total >= s:
            ans = min(ans, r - l + 1)
            total -= nums[l]
            l += 1
    return 0 if ans == len(nums) + 1 else ans


if __name__ == "__main__":
    print(minSubArrayLen(9,[1,23,3,4]))
