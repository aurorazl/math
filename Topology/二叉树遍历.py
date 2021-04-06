
#
"""
前序遍历：根结点 ---> 左子树 ---> 右子树

中序遍历：左子树---> 根结点 ---> 右子树

后序遍历：左子树 ---> 右子树 ---> 根结点
"""
def preOrderTraverse(root):
    if root:
        print(root.value)
        preOrderTraverse(root.left)
        preOrderTraverse(root.right)

def preOrderTraverse2(root):
    tmp = []
    node = root
    while tmp or node:
        if node:
            print(node.value)
            tmp.append(node)
            node = node.left
        else:
            node = tmp.pop()
            node = node.right

def inOrderTraverse(root):
    if root:
        inOrderTraverse(root.left)
        print(root.value)
        inOrderTraverse(root.right)

def inOrderTraverse2(root):
    tmp = []
    node = root
    while tmp or node:
        if node:
            tmp.append(node)
            node = node.left
        else:
            node = tmp.pop()
            print(node.value)
            node = node.right

def postOrderTraverse(root):
    if root:
        postOrderTraverse(root.left)
        postOrderTraverse(root.right)
        print(root.value)

def postOrderTraverse2(root):
    tmp = [root]
    values = []
    while tmp:
        node = tmp.pop()
        values.append(node.value)
        if node.left:
            tmp.append(node.left)
        if node.right:
            tmp.append(node.right)
    print(values[::-1])

def levelTraverse(root):
    tmp = [root]
    while tmp:
        node = tmp.pop(0)
        print(node.value)
        if node.left:
            tmp.append(node.left)
        if node.right:
            tmp.append(node.right)

class Tree:
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

f = Tree(6,None,None)
e = Tree(5,None,None)
d = Tree(4,None,None)
a = Tree(2,d,f)
b = Tree(3,e,None)
c = Tree(1,a,b)
levelTraverse(c)