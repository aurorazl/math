def Holland(li):
    begin = 0
    current = 0
    end = len(li)-1      #   定义三个指针：begin=0、current=0、end=N-1：
    while current<=end:
        if li[current]==2:
            li[end],li[current]=li[current],li[end] # 将2放到最后的位置
            end -= 1
        elif li[current]==1:     # 1表示不用变动
            current += 1
        else:
            if begin==current:  # 如果是0，放到头部
                begin += 1
                current += 1
            else:
                li[current],li[begin]=li[begin],li[current]
                begin += 1
    print(li)

def Holland2(li):
    begin = 0
    current = 0
    end = len(li)-1
    while current<=end:
        if li[current]==2:
            li[end],li[current]=li[current],li[end]
            end -= 1
        elif li[current]==1:
            current += 1
        else:                           # li[current]=0的情况
            if begin!=current:          # 如果不等，交换两者位置，这时li[current]=1
                li[current],li[begin]=li[begin],li[current]
            begin += 1
            current += 1
    print(li)
Holland([1,2,2,1,0,1,0,2])