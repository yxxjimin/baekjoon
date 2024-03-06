import sys
from collections import deque


def topologically_sort(g: dict, deg: list) -> list:
    queue = deque()
    sorted = []

    for i in range(1, len(deg)):
        if deg[i] == 0:
            queue.append(i)
    
    while queue:
        u = queue.popleft()
        sorted.append(u)
        for v in g[u]:
            deg[v] -= 1
            if deg[v] == 0:
                queue.append(v)
    
    return sorted


def main():
    num_vertex, num_edges = map(int, sys.stdin.readline().split())

    graph = {v: set() for v in range(1, num_vertex + 1)}
    in_degree = [0] * (num_vertex + 1)

    for _ in range(num_edges):
        src, dst = map(int, sys.stdin.readline().split())
        graph[src].add(dst)
        in_degree[dst] += 1

    sorted_order = topologically_sort(graph, in_degree)

    print(*sorted_order)


if __name__ == "__main__":
    main()
