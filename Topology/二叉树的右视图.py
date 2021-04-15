class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def foreachNodeList(nodeList):
    ret = []
    for one in nodeList:
        if one.left:
           ret.append(one.left)
        if one.right:
            ret.append(one.right)
    return ret

class Solution:
    def rightSideView(self, root: TreeNode):
        tmp = []
        nodeList = [root]
        while root:
            tmp.append(root.val)
            nodeList = foreachNodeList(nodeList)
            if len(nodeList)==0:
                break
            root = nodeList[-1]
        return tmp


a = {"1":1}
for i in a:
    a[2]=1
    print(a)
