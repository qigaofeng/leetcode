def sortString(s):
    """
    :type s: str
    :rtype: str
    """
    if not s: return ''

    s = list(s)
    res = []
    while s:
        c_list = list(set(s))
        c_list.sort(key=lambda c: ord(c)) #也可以直接用c_list.sort（） 不要里面的参数
        for i in c_list:
            res.append(i)
            s.remove(i)

        c_list = list(set(s))
        c_list.sort(key=lambda c: ord(c), reverse=True)
        for i in c_list:
            res.append(i)
            s.remove(i)
    return ''.join(res)  # 把列表转换为字符串形式输出

if __name__ == "__main__":
    print(sortString("aaaaabbbbbcccc"))