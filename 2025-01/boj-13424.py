import sys


def solve():
    node_cnt, edge_cnt = map(int, sys.stdin.readline().split())
    matrix = [
        [float("inf") if i != j else 0 for i in range(node_cnt + 1)] 
        for j in range(node_cnt + 1)
    ]

    for _ in range(edge_cnt):
        src, dst, wgt = map(int, sys.stdin.readline().split())
        matrix[src][dst] = wgt
        matrix[dst][src] = wgt

    _ = sys.stdin.readline()
    friends = list(map(int, sys.stdin.readline().split()))

    # floyd-warshall
    for k in range(1, node_cnt + 1):
        for i in range(1, node_cnt + 1):
            for j in range(1, node_cnt + 1):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    
    distance_sum_list = [
        sum([matrix[i][loc] for loc in friends]) for i in range(node_cnt + 1)
    ]
    print(distance_sum_list.index(min(distance_sum_list)))
        

if __name__ == "__main__":
    for _ in range(int(sys.stdin.readline())):
        solve()
