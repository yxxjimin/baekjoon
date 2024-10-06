import sys


def bellman_ford(g: list, n: int) -> list:
    d = [float('inf')] * (n + 1)
    d[1] = 0

    for _ in range(n - 1):
        for u, v, w in g:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
    
    for u, v, w in g:
        if d[v] > d[u] + w:
            return [-1]
        
    return [d[i] if d[i] != float('inf') else -1 for i in range(2, n + 1)]


def main():
    num_vertex, num_edge = map(int, sys.stdin.readline().split())
    graph_edges = []

    for _ in range(num_edge):
        src, dst, wgt = map(int, sys.stdin.readline().split())
        graph_edges.append((src, dst, wgt))

    answer = bellman_ford(graph_edges, num_vertex)
    print(*answer, sep='\n')


if __name__ == "__main__":
    main()
