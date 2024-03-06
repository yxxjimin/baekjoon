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
    num_vertex, num_edge = map(int, sys.stdin.readline().split())
    times = [0] + list(map(int, sys.stdin.readline().split()))

    graph = {v: set() for v in range(1, num_vertex + 1)}
    parent_of = {v: set() for v in range(1, num_vertex + 1)}
    in_degree = [0] * (num_vertex + 1)

    for _ in range(num_edge):
        src, dst = map(int, sys.stdin.readline().split())
        graph[src].add(dst)
        parent_of[dst].add(src)
        in_degree[dst] += 1

    search_order = topologically_sort(graph, in_degree)

    target = int(sys.stdin.readline())

    # DP, but in topological order
    dp_table = [0] * (num_vertex + 1)
    for u in search_order:
        dp_table[u] = max([0] + [dp_table[v] for v in parent_of[u]]) + times[u]
        
        if u == target:
            break

    print(dp_table[target])


if __name__ == "__main__":
    num_cases = int(sys.stdin.readline())

    for _ in range(num_cases):
        main()
