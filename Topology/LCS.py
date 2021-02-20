
def lcs(a,b,x,y):
    if x==-1 or y==-1:
        return 0
    if a[x]==b[y]:
        length = lcs(a,b,x-1,y-1)+1
        # 到这一步的可能是两个其中一个的尝试，可能会重复，不能append来输出子序列
    else:
        length = max(lcs(a,b,x-1,y),lcs(a,b,x,y-1))
    return length

def lcs2(a,b,x,y):
    if x==len(a) or y==len(b):
        return 0
    if a[x]==b[y]:
        length = lcs2(a,b,x+1,y+1)+1
    else:
        length = max(lcs2(a,b,x+1,y),lcs2(a,b,x,y+1))
    return length

def lcs3(a,b):
    x=len(a)
    y=len(b)
    c = np.zeros((x+1, x+1))
    d = np.zeros((x+1,x+1),dtype=np.str)
    for i in range(0,x):
        for j in range(0,y):
            if a[i]==b[j]:
                c[i+1,j+1]=c[i,j]+1
                d[i+1,j+1]="↖"
            elif c[i,j+1]>=c[i+1,j]:
                c[i+1,j+1]=c[i,j+1]
                d[i+1,j+1]="↑"
            else:
                c[i+1, j+1] = c[i+1, j]
                d[i+1, j+1] = "←"
    return c,d

def show_path(a,d,i,j):
    if i==0 or j==0:
        return
    if d[i,j]=="↖":
        show_path(a,d,i-1,j-1)
        print(a[i-1])
    elif d[i,j]=="↑":
        show_path(a,d,i-1,j)
    else:
        show_path(a,d,i,j-1)



if __name__ == '__main__':
    import numpy as np
    # print(lcs("abcde","bcfde",4,4))
    # print(lcs2("abcde","bcfde",0,0))
    c,d=lcs3("abcbdab","bdcaba")
    print(d)
    print(c)
    show_path("abcbdab",d,len("abcbdab"),len("bdcaba"))