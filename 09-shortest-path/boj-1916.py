import sys, heapq


def dijkstra(g: dict, s: int, e: int) -> int:
    q = []
    heapq.heappush(q, (0, s))
    d = [float('inf')] * (len(g) + 1)
    d[s] = 0

    while q:
        dist, u = heapq.heappop(q)

        if dist > d[u]:
            continue

        if u == e:
            return d[u]
        
        for v, w in g[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heapq.heappush(q, (d[v], v))

    return -1


def main():
    num_vertices = int(sys.stdin.readline())
    num_edges = int(sys.stdin.readline())
    
    graph = {v: [] for v in range(1, num_vertices + 1)}
    for _ in range(num_edges):
        src, dst, wgt = map(int, sys.stdin.readline().split())
        graph[src].append((dst, wgt))

    src_city, dst_city = map(int, sys.stdin.readline().split())
    print(dijkstra(graph, src_city, dst_city))


if __name__ == "__main__":
    main()
