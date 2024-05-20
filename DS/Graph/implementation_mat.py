from collections import deque
import unittest

class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Graph:
    def __init__(self, adjMat):
        if not adjMat or len(adjMat)==0 or len(adjMat[0])==0:
            raise CustomError("please enter valid graph matrix.")
        self.adjMat = adjMat
        self.noOfNodes = len(adjMat)

    def bfs(self, startNode=0):
        visited = set()
        queue = deque([startNode])
        provinces = 1
        path=[]
        while(queue):
            curr = queue.popleft()
            if curr not in visited: 
                visited.add(curr)
                path.append(curr)
            for adjNode in range(self.noOfNodes):
                if self.adjMat[curr][adjNode]:
                    if adjNode not in visited: 
                        visited.add(adjNode)
                        path.append(adjNode)
                        queue.append(adjNode)
            if not queue:
                for node in range(self.noOfNodes):
                    if node not in visited:
                        provinces+=1 
                        visited.add(node)
                        path.append(node)
                        queue.append(node)
                        break
        return [path, provinces]


    def dfs(self, sourceNode=None):
        if not sourceNode: sourceNode=0
        visited = set()
        paths = []

        # calling dfs on first node and storing path on the paths list
        paths.append(self._dfs_gives_path(sourceNode, visited))
        print(f"after first {paths}")

        # calling the dfs on the components that are devoid of a connection with the first component
        for node in range(self.noOfNodes):
            if node not in visited:
                paths.append(self._dfs_gives_path(node, visited, []))

        # all the possible components dfs paths are returned here
        return paths
        
        
    def _dfs_gives_path(self, node, visited, path=[]): 
        visited.add(node)
        path.append(node)
        for adjNode in range(self.noOfNodes):
            if self.adjMat[node][adjNode]:
                if adjNode not in visited:
                    self._dfs_gives_path(adjNode, visited, path)
        return path
        



class Tests(unittest.TestCase):
    def test_bfs(self):
        adjMat = [
            [1,1,1,0,0,0],
            [1,1,0,0,0,0],
            [1,0,1,0,0,0],
            [0,0,0,1,0,0],
            [0,0,0,0,1,1],
            [0,0,0,0,1,1],
        ]
        graph = Graph(adjMat)
        path, provinces = graph.bfs()
        self.assertEqual(path, [0,1,2,3,4,5])
        self.assertEqual(provinces, 3)

    def test__dfs_gives_path(self):
        adjMat = [
            [0, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0]
        ]
        graph = Graph(adjMat)
        path = graph._dfs_gives_path(0, set(), [])
        self.assertEqual(path, [0, 1, 3, 5, 7, 2])
        
    def test_dfs(self):
        adjMat = [
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        ]
        graph = Graph(adjMat)

        # single component only test
        path = graph._dfs_gives_path(0, set(), [])
        self.assertEqual(path, [0, 1, 3, 5, 7, 2])

        # both components test
        paths = graph.dfs()
        self.assertEqual(paths, [[0, 1, 3, 5, 7, 2], [8, 9]])

unittest.main()