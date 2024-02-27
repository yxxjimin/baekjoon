import sys, heapq


def dijkstra(g: dict, n: int, s: int) -> list:
    q = []
    heapq.heappush(q, (0, s))
    d = [float('inf')] * (n + 1)
    d[0] = 0
    d[s] = 0

    while q:
        dist, u = heapq.heappop(q)

        if dist > d[u]:
            continue

        for v, w in g[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heapq.heappush(q, (d[v], v))

    return d


def main():
    num_vertex, num_edge, source = map(int, sys.stdin.readline().split())

    graph = {v: set() for v in range(1, num_vertex + 1)}
    reverse_graph = {v: set() for v in range(1, num_vertex + 1)}
    for _ in range(num_edge):
        src, dst, wgt = map(int, sys.stdin.readline().split())
        graph[src].add((dst, wgt))
        reverse_graph[dst].add((src, wgt))

    arrival = dijkstra(reverse_graph, num_vertex, source)
    departure = dijkstra(graph, num_vertex, source)

    answer = max([arrival[i] + departure[i] for i in range(num_vertex + 1)])
    print(answer)


if __name__ == "__main__":
    main()
