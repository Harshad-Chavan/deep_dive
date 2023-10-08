graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0]]


class Graph:
    def __init__(self, row, col, graph):
        self.ROW = row
        self.COL = col
        self.graph = graph

    def DFS(self, i, j, visited):


        pass

    def count_islands(self):

        # matirx for visited cells
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if not visited[i][j] and graph[i][j] == 1:
                    self.DFS(i, j, visited)
                    count += 1

        return count


row = len(graph)
col = len(graph[0])
g = Graph(row, col, graph)
g.count_islands()
