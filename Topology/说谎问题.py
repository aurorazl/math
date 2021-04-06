# 关键点：将所有人的话以及条件写成编程，然后循环所有可能即可。
# A说学校排名第一是E，B说第二是B，c说倒数第一是A，D说第一不是C，E说第一是D
# 排名第一和第二的学校说了真话

schoolSort = ["A","B","C","D","E"]
talks = {"A":False,"B":False,"C":False,"D":False,"E":False}
schools = ["A","B","C","D","E"]

def func():
    talks["A"] = schoolSort[0]=="E"
    talks["B"] = schoolSort[1]=="B"
    talks["C"] = schoolSort[4]=="A"
    talks["D"] = schoolSort[0]!="C"
    talks["E"] = schoolSort[0]=="D"
    if talks[schoolSort[0]] and talks[schoolSort[1]] and not talks[schoolSort[2]] and not talks[schoolSort[3]] and not talks[schoolSort[4]]:
        return True
    return False

def SortSchool(start,end):      # 思路一：全组合搜索
    if start>end:
        return func()
    for i in range(len(schools)):   # 每个位置可能是其中的一个，A可能放在任何一个位置。
        if schools[i]=='x':
            continue
        tmp = schools[i]
        schoolSort[start]=tmp       # 对于目前要放置的位置，放置还没放入的一个，然后start+1，放置下一个
        schools[i]="x"              # 标记为已用
        if SortSchool(start+1,end):
            return True
        schools[i]=tmp              # 放回，使得可用，这是递归的精髓
    return False

from itertools import combinations_with_replacement,permutations        # 组合所有可能
def sort2():
    for i in permutations(schools,5):
        global schoolSort
        schoolSort = i
        if func():
            return True
    return False

# SortSchool(0,4)
sort2()
print(schoolSort)
