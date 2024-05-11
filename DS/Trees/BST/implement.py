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


bst = BST()
for x in [3, 7, 4, 5, 2, 1]: bst.insert(x)
bst.bfs()