import sys, heapq


def dijkstra(g: dict, n: int, s: int, e: int) -> int | float:
    q = []
    heapq.heappush(q, (0, s))
    d = [float('inf')] * (n + 1)
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
                heapq.heappush(q, (d[v] , v))
    
    return d[e]


def main():
    num_vertex, num_edge = map(int, sys.stdin.readline().split())
    graph = {v: set() for v in range(1, num_vertex + 1)}
    for _ in range(num_edge):
        src, dst, wgt = map(int, sys.stdin.readline().split())
        graph[src].add((dst, wgt))
        graph[dst].add((src, wgt))

    stop_1, stop_2 = map(int, sys.stdin.readline().split())

    case_1 = (dijkstra(graph, num_vertex, 1, stop_1)
              + dijkstra(graph, num_vertex, stop_1, stop_2)
              + dijkstra(graph, num_vertex, stop_2, num_vertex))
    
    case_2 = (dijkstra(graph, num_vertex, 1, stop_2)
              + dijkstra(graph, num_vertex, stop_2, stop_1)
              + dijkstra(graph, num_vertex, stop_1, num_vertex))
    
    answer = min(case_1, case_2)

    if answer == float('inf'):
        print(-1)
    else:
        print(answer)


if __name__ == "__main__":
    main()
