###
"""
前序遍历：根节点->左子树->右子树
中序遍历：左子树->根节点->右子树
后序遍历：左子树->右子树->根节点
"""

# 递归法，比较简单
def preOrderTraverse(node):
    if not node:
        return None
    print(node.val)                         # 调整顺序即可
    preOrderTraverse(node.left)
    preOrderTraverse(node.right)

# 非递归法
def preOrderTravese(node):          # 第一次访问就输出数据
    stack = [node]
    while len(stack) > 0:
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        node = stack.pop()

def inOrderTraverse(node):      # 应用场景：二叉查找树，从小到大出栈
    stack = []
    pos = node
    while pos or len(stack) > 0:
        if pos:
            stack.append(pos)
            pos = pos.left
        else:
            pos = stack.pop()
            print(pos.val)
            pos = pos.right


def postOrderTraverse(node):        #对节点操作时必访问过其子节点，适合进行破坏性操作（删除节点）
    stack = [node]
    stack2 = []
    while len(stack) > 0:
        node = stack.pop()
        stack2.append(node)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    while len(stack2) > 0:
        print(stack2.pop().val)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(postOrderTraverse(a))
