def lastRemaining(self, n, m):
    ans = 0
    for i in range(2, n + 1):
        ans = (ans + m) % i
    return ans

if __name__ == "__main__":
    print(lastRemaining(5,3))
