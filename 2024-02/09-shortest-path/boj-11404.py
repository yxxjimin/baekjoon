import sys


def main():
    num_vertex = int(sys.stdin.readline())
    num_edge = int(sys.stdin.readline())
    graph = [[0 if i == j else float('inf') for i in range(num_vertex + 1)]
             for j in range(num_vertex + 1)]
    
    for _ in range(num_edge):
        src, dst, wgt = map(int, sys.stdin.readline().split())
        if graph[src][dst] > wgt:
            graph[src][dst] = wgt

    for k in range(1, num_vertex + 1):
        for i in range(1, num_vertex + 1):
            for j in range(1, num_vertex + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, num_vertex + 1):
        print(*[x if x != float('inf') else 0 for x in graph[i][1:]])


if __name__ == "__main__":
    main()
