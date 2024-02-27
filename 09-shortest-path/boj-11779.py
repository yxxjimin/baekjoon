import sys, heapq


def dijkstra(g: dict, s: int, e: int) -> tuple[int, list]:
    q = []
    heapq.heappush(q, (0, s))
    d = [[float('inf'), None] for _ in range(len(g) + 1)]
    d[s][0] = 0

    while q:
        dist, u = heapq.heappop(q)

        if dist > d[u][0]:
            continue

        if u == e:
            break

        for v, w in g[u]:
            if d[v][0] > d[u][0] + w:
                d[v][0] = d[u][0] + w
                d[v][1] = u
                heapq.heappush(q, (d[v][0], v))
    
    v = e
    path = [v]
    while d[v][1] is not None:
        pred = d[v][1]
        path.append(pred)
        v = pred
    path.reverse()
    
    return d[e][0], path


def main():
    num_vertex = int(sys.stdin.readline())
    num_edge = int(sys.stdin.readline())

    graph = {v: set() for v in range(1, num_vertex + 1)}
    for _ in range(num_edge):
        src, dst, wgt = map(int, sys.stdin.readline().split())
        graph[src].add((dst, wgt))

    source, destination = map(int, sys.stdin.readline().split())
    length, path = dijkstra(graph, source, destination)

    print(length)
    print(len(path))
    print(*path)


if __name__ == "__main__":
    main()
