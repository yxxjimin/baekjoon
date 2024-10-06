import sys, heapq


def dijkstra(g: dict, s: int, k: int) -> list:
    q = []
    heapq.heappush(q, (0, s))
    d = [sys.maxsize] * (len(g) + 1)
    d[s] = 0

    answer = []
    while q:
        dist, u = heapq.heappop(q)

        if d[u] < dist:
            continue

        if dist == k:
            answer.append(u)
            continue

        for v in g[u]:
            if d[v] > d[u] + 1:
                d[v] = d[u] + 1
                heapq.heappush(q, (d[v], v))

    return answer


def main():
    num_city, num_edge, tgt_dist, src_city = map(int, sys.stdin.readline().split())

    adj_list = {v: set() for v in range(1, num_city + 1)}
    for _ in range(num_edge):
        src, dst = map(int, sys.stdin.readline().split())
        adj_list[src].add(dst)

    answer = dijkstra(adj_list, src_city, tgt_dist)

    if answer:
        print(*answer, sep='\n')
    else:
        print(-1)


if __name__ == "__main__":
    main()
