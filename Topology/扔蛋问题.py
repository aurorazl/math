li=[]
def egg_search(egg_nums,layers,start,end):
    if egg_nums<=1:
        return end-start+1
    if layers==0:
        return 0
    if layers==1:
        return 1
    if end<=start:
        return 1
    min = layers
    mid = (start+end)//2
    a = egg_search(egg_nums-1,layers,start,mid-1)+1
    b = egg_search(egg_nums,layers,mid+1,end)+1
    v = max(a,b)
    if min>v:
        min=v
    return min

print(egg_search(6,100,1,100))

# 只要鸟蛋数达到 num>=math.ceil(log2(layers))，即可在二分数内试出次数，如果小于，基本上就是n-1次二分后剩下的楼层需要一层层来试，即  math.ceil(layers/(2**(num-1)))+nums-1
