
def CalcNext(p):
    n = len(p)
    Next = [-1]
    k = -1      # 上一次重复部分应该回到的位置，Next的值
    j = 0       # 字符串的指针，从1开始比较
    while j<n-1:
        if k==-1 or p[j]==p[k]: # k==-1表示首次分析，和从未出现过的情况
            k += 1              # 先+1，跳过首次分析，和从未出现过的情况
            j += 1
            Next.append(k)    # 如果相等，next[j+1]=next[j]+1，比较下一位
        else:
            k = Next[k]
    return Next
# print(CalcNext('abaabcaba'))
def CalcNext2(p):
    n = len(p)
    Next = [-1]
    k = -1      # 上一次重复部分应该回到的位置，Next的值
    j = 0       # 字符串的指针，从1开始比较
    while j<n-1:
        if k==-1 or p[j]==p[k]: # k==-1表示首次分析，和从未出现过的情况
            k += 1              # 先+1，跳过首次分析，和从未出现过的情况
            j += 1
            if p[j]==p[k]:              # +1后相等，表示第 k 位 的模式串也不用匹配了，直接回滚到next[k]的模式串位置
                Next.append(Next[k])    # 如果相等，next[j+1]=next[j]+1，比较下一位
            else:
                Next.append(k)
        else:
            k = Next[k]
    return Next
# print(CalcNext2('abaabcaba'))
def KMP(string,parttern):
    ans = -1    # 模式串第一次出现位置
    i = 0
    j = 0
    Next = CalcNext(parttern)
    parttern_len = len(parttern)
    string_len = len(string)
    while i < string_len :  # 大于时表示已经匹配失败
        if j == -1 or string[i] == parttern[j]: # 如果字符串匹配，或者j=-1表示回到首位，继续j+1=0开始匹配
            i += 1
            j += 1
        else:
            j = Next[j]
        if j == parttern_len:   # 已经超过模式串长度，表示匹配完成，返回当前开头的位置
            ans = i- parttern_len
            break
    return ans
print(KMP('abcdef','ef'))