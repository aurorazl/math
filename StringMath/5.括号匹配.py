class Stack(object):
    def __init__(self):
        self.stack = []
    def pop(self):
        return self.stack.pop()
    def push(self,val):
        return self.stack.append(val)
    def empty(self):
        return len(self.stack)==0
    def top(self):
        return self.stack[-1]

def Solution(s):
    left = "([{"
    right = ")]}"
    stk = Stack()
    for i in s:
        if i in left:
            stk.push(i)
        else:
            if stk.empty() or stk.top()!=left[right.find(i)]:
                return False
            else:
                stk.pop()
    return stk.empty()
# print(Solution('([)]'))

def longestValidParentheses(s):
    stk = Stack()
    last_unvalid_pos = -1
    max_len = 0
    for i in range(len(s)):
        if s[i] == '(':
            stk.push(i)
        else:
            if stk.empty():
                last_unvalid_pos = i    # 记录上一次不匹配时的下标，用于判断总长度
            else:
                stk.pop()
                if stk.empty():
                    max_len = max(max_len,i-last_unvalid_pos)   # 栈为空了，此时算一下自不匹配以来的长度
                else:
                    max_len = max(max_len, i - stk.top())       # 栈不空，算一下目前最长匹配长度
    return max_len
print(longestValidParentheses(')()(())'))

def longestValidParentheses2(s):
    last_unvalid_pos = -1
    max_len = 0
    deep=0
    n = len(s)
    for i in range(n):
        if s[i] == '(':
            deep += 1
        else:
            deep -= 1
            if deep<0:
                last_unvalid_pos = i    # 记录上一次不匹配时的下标，用于判断总长度
                deep = 0
            elif deep == 0:
                max_len = max(max_len,i-last_unvalid_pos)
    deep = 0
    last_unvalid_pos = n
    for i in range(n-1,-1,-1):
        if s[i] == ')':         # 从右扫描，以避免左括号大于右括号的情况
            deep += 1
        else:
            deep -= 1
            if deep<0:
                last_unvalid_pos = i    # 记录上一次不匹配时的下标，用于判断总长度
                deep = 0
            elif deep == 0:
                max_len = max(max_len,i-last_unvalid_pos)
    return max_len
print(longestValidParentheses2(')()(())'))