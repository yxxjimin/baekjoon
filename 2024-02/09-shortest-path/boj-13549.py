import heapq


def dijkstra(g: dict, s: int, t: int) -> int:
    q = []
    heapq.heappush(q, (0, s))
    d = [float('inf')] * (len(g) + 1)
    d[s] = 0

    while q:
        dist, u = heapq.heappop(q)

        if dist > d[u]:
            continue

        if u == t:
            return d[u]
        
        for v, w in g[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heapq.heappush(q, (d[v], v))

    return -1


def main():
    src, dst = map(int, input().split())

    graph = {v: [] for v in range(100001)}
    for v in range(100001):
        if v > 0:
            graph[v].append((v - 1, 1))
        if v < 100000:
            graph[v].append((v + 1, 1))
            if v < 50001:
                graph[v].append((v * 2, 0))
    
    print(dijkstra(graph, src, dst))


if __name__ == "__main__":
    main()
