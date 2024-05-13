class Node():
    def __init__(self, value: int) -> None:
        self.data = value
        self.left = None
        self.right = None
    def getData(self):
        return self.data
    def setData(self, value):
        self.data = value

class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val, curr=None):
        if (not self.root):
            self.root = Node(val)
            return
        if (not curr):
            curr = self.root
        if (val < curr.getData()):
            if (curr.left):
                return self.insert(val, curr.left)
            else:
                curr.left = Node(val)
                return 
        elif(val>curr.getData()):
            if(curr.right):
                return self.insert(val, curr.right)
            else:
                curr.right = Node(val)
                return

        
    def bfs(self):
        if (not self.root):
            return -1
        queue = [self.root]
        bfsArr = []
        while(queue):
            curr = queue[0]
            bfsArr.append(curr.getData())
            queue = queue[1:]
            if (curr.left):
                queue.append(curr.left)
            if (curr.right): queue.append(curr.right)
        print(bfsArr)

    def inorder(self, node=None):
        if not node:
            if not self.root:
                return
            node = self.root 
        if node.left: self.inorder(node.left)
        print(node.getData())
        if node.right: self.inorder(node.right)

    def preOrder(self, node=None):
        if not node:
            if not self.root: return
            node = self.root
        print(node.getData())
        if node.left: self.preOrder(node.left)
        if node.right: self.preOrder(node.right)
    
    def postOrder(self, node=None):
        if not node:
            if not self.root: return
            node = self.root
        if node.left: self.postOrder(node.left)
        if node.right: self.postOrder(node.right)
        print(node.getData())

bst = BST()
for x in [11, 23, 9, 13]: bst.insert(x)
# bst.bfs()
# bst.inorder()
# bst.preOrder()
bst.postOrder()