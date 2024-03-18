import sys


def main():
    num_vertices, num_edges = map(int, sys.stdin.readline().split())
    graph = [[0 if i == j else float('inf') for i in range(num_vertices + 1)] 
             for j in range(num_vertices + 1)]
    
    for _ in range(num_edges):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1
        graph[b][a] = 1

    for k in range(1, num_vertices + 1):
        for i in range(1, num_vertices + 1):
            for j in range(1, num_vertices + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    answers = [sum(graph[i][1:]) for i in range(num_vertices + 1)]
    smallest_idx = 0
    for idx in range(len(answers)):
        if answers[idx] < answers[smallest_idx]:
            smallest_idx = idx

    print(smallest_idx)


if __name__ == "__main__":
    main()
