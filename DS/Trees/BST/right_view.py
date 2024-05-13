class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            self.insert_service(self.root, value)
        else:
            self.root = Node(value)

    def insert_service(self, node, value):
        if (value < node.data):
            if node.left:
                return self.insert_service(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                return self.insert_service(node.right, value)
            else:
                node.right = Node(value)

    def bfs(self, node=None):
        if not node:
            if not self.root: 
                return
            node = self.root
        queue = [node]
        while(queue):
            current = queue[0]
            queue = queue[1:]
            print(current.data)
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)

    def rhv(self):
        ans = []
        if not self.root: return
        self.rhv_service(self.root, 0, ans)
        return ans


    def rhv_service(self, node, depth, ans):
        if (len(ans)==depth): ans.append(node.data)
        if (node.right): self.rhv_service(node.right, depth+1, ans)
        if (node.left): self.rhv_service(node.left, depth+1, ans)


# arr = [11, 9, 23, 13]
arr = [11, 9, 23, 13, 3, 1]
tree = BST()
for x in arr: tree.insert(x)
# tree.bfs()
print(*tree.rhv())
