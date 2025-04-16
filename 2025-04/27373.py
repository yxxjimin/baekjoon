import sys


INF = float("inf")


class Graph:
    size: int
    dist: list[list[list[int | float]]]
    history: list[bool]
    scores: list[int]

    def __init__(self, n: int):
        self.size = n
        self.dist = [[
            [INF if i != j else 0 for i in range(n + 1)] for j in range(n + 1)
        ]]
        self.history = []
        self.scores = []
    
    def construct_edge(self, src: int, dst: int, wgt: int):
        if wgt < self.dist[-1][src][dst]:
            self.dist[-1][src][dst] = wgt
            self.dist[-1][dst][src] = wgt

    def floyd_warshall(self):
        for k in range(1, self.size + 1):
            for i in range(1, self.size + 1):
                for j in range(1, self.size + 1):
                    min_dist = min(
                        self.dist[-1][i][j], 
                        self.dist[-1][i][k] + self.dist[-1][k][j]
                    )
                    self.dist[-1][i][j] = min_dist
                    self.dist[-1][j][i] = min_dist

        score = 0
        for i in range(1, self.size + 1):
            for j in range(i + 1, self.size + 1):
                if self.dist[-1][i][j] < INF:
                    score += self.dist[-1][i][j]
        self.scores.append(score)

    def _add_layer(self, src: int, dst: int, wgt: int):
        new_dist = [[d for d in row] for row in self.dist[-1]]
        new_dist[src][dst] = wgt
        new_dist[dst][src] = wgt
        score = 0
        
        for i in range(1, self.size + 1):
            for j in range(i + 1, self.size + 1):
                min_dist = min(
                    new_dist[i][j],
                    new_dist[i][src] + wgt + new_dist[dst][j],
                    new_dist[i][dst] + wgt + new_dist[src][j]
                )
                new_dist[i][j] = min_dist
                new_dist[j][i] = min_dist

                if min_dist < INF:
                    score += min_dist
            
        self.dist.append(new_dist)
        self.scores.append(score)

    def _pop_layer(self):
        self.dist.pop()
        self.scores.pop()
    
    def op_calculate_score(self) -> int:
        return self.scores[-1]

    def op_add_edge(self, src: int, dst: int, wgt: int):
        if wgt < self.dist[-1][src][dst]:
            self.history.append(True)
            self._add_layer(src, dst, wgt)
        else:
            self.history.append(False)
            
    def op_pop_edge(self):
        if len(self.history) > 0:
            if self.history.pop():
                self._pop_layer()


def main():
    for _ in range(int(sys.stdin.readline())):
        n, m, q = map(int, sys.stdin.readline().split())
        graph = Graph(n)
        results = []

        for _ in range(m):
            src, dst, wgt = map(int, sys.stdin.readline().split())
            graph.construct_edge(src, dst, wgt)

        graph.floyd_warshall()

        for _ in range(q):
            line = list(map(int, sys.stdin.readline().split()))
            if len(line) == 1 and line[0] == 1:
                results.append(graph.op_calculate_score())
            elif len(line) == 1 and line[0] == 3:
                graph.op_pop_edge()
            else:
                _, src, dst, wgt = line
                graph.op_add_edge(src, dst, wgt)
        
        print(*results)


if __name__ == "__main__":
    main()
