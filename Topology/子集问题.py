## 求字符串的所有子集
"""
比如"AB"的所有子集为"","A","B","AB"
"""

# 迭代法，有点像深度优先
def stringSubSet(s):
    tmp = [""]
    for i in s:
        tmp += [j+i for j in tmp]
    return tmp

print(stringSubSet("abc"))

# 回溯思想
def stringSubSet2(s):
    res = []
    n = len(s)
    def search(i, tmp):
        res.append(tmp)
        for j in range(i, n):
            search(j + 1, tmp + s[j])
    search(0, "")
    return res
print(stringSubSet2("abc"))

### 深度优先2
def stringSubSet3(s):
    res = [""]
    n = len(s)
    for i in range(n):
        tmp = [s[i]]
        for j in range(i+1,n):
            tmp += [one+s[j] for one in tmp]
        res += tmp
    return res

print(stringSubSet3("abc"))

# 字符串中包含重复
def repeatableStringSubSet(s):
    res = []
    n = len(s)

    def search(i, tmp):
        if tmp not in res:
            res.append(tmp)
        for j in range(i, n):
            search(j + 1, tmp + s[j])

    search(0, "")
    return res
print(repeatableStringSubSet("abca"))