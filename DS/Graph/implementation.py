import unittest

class Graph:
    def __init__(self, noOfVertices, edges) -> None:
        self.noOfVertices = noOfVertices
        self.adjList = [[] for i in range(noOfVertices)]
        for x, y in edges:
                self.adjList[x].append(y)
                self.adjList[y].append(x)
    
    def bfs(self, node):
        if node is None: return
        visited = [False]*self.noOfVertices
        def _bfs(node):
            queue = [node]
            visited[node] = True
            while(queue):
                curr = queue[0]
                queue = queue[1:]
                print(curr)
                for neighbour in self.adjList[curr]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        queue.append(neighbour)

        _bfs(node)
        for i in range (len(visited)):
            if not visited[i]:
                _bfs(i)


    def r_dfs(self, node):
        if node is None: return
        visited = [False]*self.noOfVertices
        visited[node] = True
        ans = [node]
        def _r_dfs(node):
            if node is None: return
            for neighbour in self.adjList[node]:
                if not visited[neighbour]:
                    ans.append(neighbour)
                    visited[neighbour] = True
                    _r_dfs(neighbour)

        _r_dfs(node)
        for i in range(self.noOfVertices):
            if not visited[i]:
                _r_dfs(i) 
        return ans



class Test(unittest.TestCase):

    def test_bfs(self):
        noOfVertices = 11
        edges = [
            [0, 1],
            [0, 2],
            [0, 3],
            [0, 4],
            [0, 5],
            [0, 6],
            [2, 7],
            [4, 8],
            [8, 9],
            [3, 10]
        ]
        graph = Graph(noOfVertices, edges)
        # graph.bfs(8)
        graph.r_dfs(0)

        # // above 2 works just find answers and make cases below to check

    def test_r_dfs(self):
        noOfVertices = 11
        edges = [
            [0, 1],
            [0, 2],
            [0, 3],
            [0, 4],
            [0, 5],
            [0, 6],
            [2, 7],
            [4, 8],
            [8, 9],
            [3, 10]
        ]
        graph = Graph(noOfVertices, edges)
        self.assertEqual(graph.r_dfs(0), [0, 1, 2, 7, 3, 10, 4, 8, 9, 5, 6])
        self.assertEqual(graph.r_dfs(4), [4, 0, 1, 2, 7, 3, 10, 5, 6, 8, 9])

unittest.main()