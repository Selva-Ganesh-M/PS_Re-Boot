import unittest
graph_data = [
    {
    "noOfVertices": 5,
    "edges": [[0, 1], [0, 2], [1, 3], [2, 3]]
    },
    {
    "noOfVertices": 6,
    "edges": [[0, 1], [0, 2], [3, 4], [4, 5]]
    },
    {
    "noOfVertices": 4,
    "edges": [[0, 1], [2, 3]]  # Two disconnected components
    },
    {
    "noOfVertices": 7,
    "edges": [[0, 1], [0, 2], [1, 3], [2, 4], [5, 6]]  # Two components
    },
    {
    "noOfVertices": 8,
    "edges": [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7]]
    },
    {
    "noOfVertices": 0,
    "edges": []
    },
    {
    "noOfVertices": 3,
    "edges": [[0, 0]]  # This is an edge from a vertex to itself
    },
    {
    "noOfVertices": 1,
    "edges": []
    },
    {
    "noOfVertices": 5,
    "edges": [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    },
    {
    "noOfVertices": 5,
    "edges": [[0, 1], [2, 3]]  # Only two edges connecting distant vertices
    }
]
class Graph:
    def __init__(self, noOfVertices, edges):
        self.noOfVertices = noOfVertices
        self.adjList = [[]]*self.noOfVertices
        for x, y in edges:
            self.adjList[x] = y
            self.adjList[y] = x

    def getBfs(self, source):
        if not source: return
        visited = set()
        ans = []
        queue = [source]
        while(queue):
            curr = queue[0]
            queue = queue[1:]

class Test(unittest.TestCase):
    def test_bfs(self):
        case_data = graph_data[0]
        graph = Graph(case_data.get("noOfVertices"), case_data.get("edges"))
        self.assertEqual(graph.getBfs(0), [0, 1, 2, 3])


unittest.main()