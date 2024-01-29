import sys
sys.setrecursionlimit(50000)

def get_adj_nodes(
        row: int, col: int, row_max: int, col_max: int) -> list[(int, int)]:
    
    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    nodes = []
    for new_r, new_c in [(row + dy, col + dx) for dy, dx in dxdy]:
        if new_r in range(row_max) and new_c in range(col_max):
            nodes.append((new_r, new_c))
    
    return nodes


def dfs(row: int, col: int):
    farm[row][col] = 2
    adj_nodes = get_adj_nodes(row, col, n, m)
    for adj_r, adj_c in adj_nodes:
        if farm[adj_r][adj_c] == 1:
            dfs(adj_r, adj_c)


num_cases = int(input())
for _ in range(num_cases):
    m, n, k = map(int, input().split())
    
    farm = [[0] * m for _ in range(n)]
    for _ in range(k):
        col, row = map(int, input().split())
        farm[row][col] = 1

    connected_components = 0
    for src_r in range(n):
        for src_c in range(m):
            if farm[src_r][src_c] == 1:
                connected_components += 1
                dfs(src_r, src_c)
    
    print(connected_components)


# # Stack version
#
# def main():
#     # Read graph
#     m, n, k = map(int, input().split())
#    
#     farm = [[0] * m for _ in range(n)]
#     for _ in range(k):
#         col, row = map(int, input().split())
#         farm[row][col] = 1
#    
#     # DFS
#     stack = []
#     connected_components = 0
#     for src_r in range(n):
#         for src_c in range(m):
#             if farm[src_r][src_c] == 1:
#                 connected_components += 1
#                 stack.append((src_r, src_c))
#                 while stack:
#                     r, c = stack.pop()
#                     farm[r][c] = 2 # Visited
#                     adj_nodes = get_adj_nodes(r, c, n, m)
#                     for adj_r, adj_c in adj_nodes:
#                         if farm[adj_r][adj_c] == 1:
#                             stack.append((adj_r, adj_c))
#
#     print(connected_components)
#
#
# num_cases = int(input())
# for _ in range(num_cases):
#     main()
#