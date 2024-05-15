import unittest

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def clear(self):
        self.root = None

    def insert(self, value, source=None):
        if not value: return
        if not self.root: 
            self.root = Node(value)
            return
        if not source: source = self.root
        if value < source.data:
            if not source.left:
                source.left = Node(value)
                return
            return self.insert(value, source.left)
        else:
            if not source.right:
                source.right = Node(value)
                return
            return self.insert(value, source.right)

    def bfs(self):
        if not self.root: return []
        queue = [self.root]
        res = []
        while (queue):
            curr = queue[0]
            queue = queue[1:]
            res.append(curr.data)
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        return res
            

    def r_dfs (self, source=None, visited = []):
        def dfs(source):
            visited.append(source.data)
            if source.left:
                dfs(source.left)
            if source.right:
                dfs(source.right)
        if not source:
            if not self.root: return visited
            source = self.root
        dfs(source)
        return visited

    def s_dfs(self):
        res = []
        if not self.root: return res
        stack = [self.root]
        while(stack):
            curr = stack.pop()
            res.append(curr.data)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res





class Test(unittest.TestCase):

    def test_main(self):
        
        # case: 1
        bst = BinarySearchTree()

        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(7)
        bst.insert(9)

        # test insert function
        self.assertEqual(bst.root.data, 10)
        self.assertEqual(bst.root.left.data, 5)
        self.assertEqual(bst.root.left.right.data, 7)
        self.assertEqual(bst.root.left.right.right.data, 9)
        self.assertEqual(bst.root.right.data, 15)


        # test bfs function
        self.assertEqual(bst.bfs(), [10, 5, 15, 7, 9])

        # test r_dfs function
        self.assertEqual(bst.r_dfs(), [10, 5, 7, 9, 15])

        # test s_dfs function
        self.assertEqual(bst.s_dfs(), [10, 5, 7, 9, 15])

        # case: 2
        bst.clear()

unittest.main()