
def func(changes,k):
    tmp = {i:0 for i in range(1,k+1)}
    for i in changes:
        key = sorted(list(tmp.keys()),reverse=True)
        for j in key:
            if not j+i in key:
                tmp[j + i] = 0
            tmp[j+i] += tmp[j]
        if i not in key:
            tmp[i]=1
        else:
            tmp[i] += 1
    print(tmp)
    return tmp[k] if k in tmp else None



print(func([2,3,5],6))