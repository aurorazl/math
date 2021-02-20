def LongestPalindrome(s):
    n = len(s)
    if n<1:
        return 0
    max = 0
    for i in range(n):
        j = 0
        while i-j>=0 and i+j <n:
            if s[i-j] != s[i+j]:
                break
            if j*2+1>max:
                max = j*2+1
            j += 1
        j = 0
        while i-j>=0 and i+j+1 <n:
            if s[i-j] != s[i+j+1]:
                break
            if j*2+2>max:
                max = j*2+2
            j += 1
    return max

# print(LongestPalindrome('aba'))

def Manacher(s):
    n = len(s)
    p = [1 for i in range(n)]       # 记录以字符S[i]为中心的最长回文子串向左/右扩张的长度(包括S[i])
    id = 0
    mx = 1
    for i in range(1,n):
        if mx>i:
            p[i] = min(p[2*id-i],mx-i)  # mx-i属于部分控制了i，超出的部分通过暴力左右判断即可
        else:
            p[i]=1
        while i-p[i]>=0 and i+p[i]<n and  s[i+p[i]] == s[i-p[i]]:   # 对于已经超出mx的i，循环判断左右值是否相等
            p[i] += 1
        if mx<i+p[i]:
            mx = i+p[i]
            id = i
    return p

def Manacher2(s):
    n = len(s)
    p = [1 for i in range(n)]
    id = 0
    mx = 1
    for i in range(1,n):
        if mx>i:
            if p[2*id-i] != mx-i:           # 无论是p[2*id-i]大于（mx右侧部分和i-mx左侧已经不相等了，不用再扩展了），小于就再范围内，不用扩展
                p[i] = min(p[2*id-i],mx-i)  # 对于超出部分，如果p[2*id-i]大于mx-i，经验证明p[i]=mx-i
            else:
                p[i]=p[2*id-i]
                while i - p[i] >= 0 and i + p[i] < n and s[i + p[i]] == s[i - p[i]]:  # P[i] ≥P[j]
                    p[i] += 1
        else:
            p[i]=1
            while i-p[i]>=0 and i+p[i]<n and  s[i+p[i]] == s[i-p[i]]:   # 对于已经超出mx的i，循环判断左右值是否相等
                p[i] += 1
        if mx<i+p[i]:
            mx = i+p[i]
            id = i
    return p
print(Manacher2('$#a#b#a#'))