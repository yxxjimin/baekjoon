import sys, heapq


def topological_sort(g: dict, deg: list) -> list:
    queue = []
    for u in range(1, len(deg)):
        if deg[u] == 0:
            heapq.heappush(queue, u)
    
    result = []
    while queue:
        u = heapq.heappop(queue)
        result.append(u)

        for v in g[u]:
            deg[v] -= 1
            if deg[v] == 0:
                heapq.heappush(queue, v)

    return result


def main():
    num_vertex, num_edge = map(int, sys.stdin.readline().split())
    graph = {v: set() for v in range(1, num_vertex + 1)}
    in_degree = [0] * (num_vertex + 1)

    for _ in range(num_edge):
        src, dst = map(int, sys.stdin.readline().split())
        graph[src].add(dst)
        in_degree[dst] += 1
    
    answer = topological_sort(graph, in_degree)

    print(*answer)


if __name__ == "__main__":
    main()