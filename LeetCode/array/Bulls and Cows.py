import collections


def getHint(secret, guess):
    """
        1. 先计算相等的字符a的个数.
        2. 把不相等的字符进行数量的统计, 然后计算b的个数
    """
    a, b, s1, s2 = 0, 0, [], []
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            a += 1
            #print(secret[i])  实际的值
        else:
            s1.append(secret[i])
            s2.append(guess[i])
            #print(s1)   ['1']
    counter1, counter2 = collections.Counter(s1), collections.Counter(s2)#counter 1,2 是字典了，所有后面有key
    print(s1)       #key 就是value ;  key后面的值代表value出现的次数
    #print(counter1)  # counter 就是一个完整的字典，有key有value
    for k in counter1.keys():
        if k in counter2.keys():
            b += min(counter1[k], counter2[k])

    return "{A}A{B}B".format(A=a,B=b)

if __name__ == "__main__":
    print(getHint("1123", "0111"))

