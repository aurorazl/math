string = [1,2,2,4]
n = len(string)
def Permutation(start,end):
    if start == end-1:
        print(string)
        return
    for i in range(start,end):
        if IsSwap(start,i):
            continue
        string[i],string[start] = string[start],string[i]   # 当前循环先交换
        Permutation(start+1,end)
        string[i],string[start] = string[start],string[i]   # 再换回来，这样下一个i交换时还是1234


def IsSwap(start,i):
    flag = False
    for i in range(start,i):
        if string[i]==string[i]:  # 如果前面已经存在，就不交换
            flag = True
            break
    return flag

Permutation(0,n)