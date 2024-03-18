import sys
from collections import deque


def get_topological_order(g: dict, deg: list) -> list:
    queue = deque()
    depth = [0] * len(deg)
    
    dist = 1
    for i in range(1, len(deg)):
        if deg[i] == 0:
            queue.append(i)
            depth[i] = dist

    while queue:
        dist += 1
        for _ in range(len(queue)):
            u = queue.popleft()
            for v in g[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    queue.append(v)
                    depth[v] = dist

    return depth[1:]


def main():
    num_vertex, num_edge = map(int, sys.stdin.readline().split())
    graph = {v: set() for v in range(1, num_vertex + 1)}
    in_degree = [0] * (num_vertex + 1)

    for _ in range(num_edge):
        src, dst = map(int, sys.stdin.readline().split())
        graph[src].add(dst)
        in_degree[dst] += 1

    answer = get_topological_order(graph, in_degree)

    print(*answer)
    

if __name__ == "__main__":
    main()
