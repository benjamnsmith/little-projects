'''
Rules That Every Red-Black Tree Follows: 
1. Every node has a colour either red or black.
2. The root of the tree is always black.
3. There are no two adjacent red nodes (A red node cannot have a red parent or red child).
4. Every path from a node (including root) to any of its descendants NULL nodes has the same number of black nodes.
5. All leaf nodes are black nodes.
'''

from node import *


class RedBlack():
    def __init__(self, dat = None):
        self.root = dat
        return


    def __rotateLeft(curNode : Node):
        x = curNode.right
        y = x.left
        x.left = curNode
        curNode.right = y
        curNode.parent = x
        if (y is not None):
            y.parent = curNode
        return x

    def __rotateRight(curNode : Node):
        x = curNode.left
        y = x.right
        x.right = curNode
        curNode.left = y
        curNode.parent = x
        if (y is not None):
            y.parent = curNode
        return x

    ll = False
    rr = False
    lr = False
    rl = False
    def __insertHelp(self, curNode : Node, val):
        conflict = False
        if curNode is None:
            return(Node(val))
        elif (val < curNode.data):
            curNode.left = self.__insertHelp(curNode.left, val)
            curNode.left.parent = curNode
            if curNode is not self.root:
                if(curNode.color == 'R' and curNode.left.color == 'R'):
                    conflict = True
        else:
            curNode.right = self.__insertHelp(curNode.right, val)
            curNode.right.parent = curNode
            if curNode is not self.root:
                if curNode.color == 'R' and curNode.right.color == 'R':
                    conflict = True
        if self.ll:
            curNode = self.__rotateLeft(curNode)
            curNode.color = 'B'
            curNode.left.color = 'R'
            self.ll = False
        elif self.rr:
            curNode = self.__rotateRight(curNode)
            curNode.color = 'B'
            curNode.right.color = 'R'
            self.rr = False
        elif self.rl:
            curNode.right = self.__rotateRight(curNode.right)
            curNode.right.parent = curNode
            curNode = self.__rotateLeft(curNode)
            curNode.color = 'B'
            curNode.left.color = 'R'
            self.rl = False
        elif self.lr:
            curNode.left = self.__rotateLeft(curNode.left)
            curNode.left.parent = curNode
            curNode = self.__rotateRight(curNode)
            curNode.color = 'B'
            curNode.right.color = 'R'
            self.lr = False
        
        if conflict:
            return


    def insert(self, val):
        if (self.root == None):
            self.root = Node(val)
            self.root.color = 'B'
        else:
            self.__insertHelp(self.root, val)


