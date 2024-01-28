num_vertices, num_edges, src = map(int, input().split())

# Read graph
adj_list = {}
for _ in range(num_edges):
    u, v = map(int, input().split())

    if u not in adj_list:
        adj_list[u] = set()
    adj_list[u].add(v)

    if v not in adj_list:
        adj_list[v] = set()
    adj_list[v].add(u)

# DFS
dfs_path = []
dfs_visited = [False] * num_vertices
def dfs(node: int):
    dfs_visited[node - 1] = True
    dfs_path.append(str(node))
    adj_nodes = list(adj_list[node]) if node in adj_list else []
    adj_nodes.sort() # Small number first
    for adj_node in adj_nodes:
        if not dfs_visited[adj_node - 1]:
            dfs(adj_node)

dfs(src)
print(' '.join(dfs_path))

# BFS
bfs_path = []
bfs_visited = [False] * num_vertices
bfs_visited[src - 1] = True
bfs_queue = [src]
while len(bfs_queue) > 0:
    node = bfs_queue.pop(0)
    bfs_path.append(str(node))
    adj_nodes = list(adj_list[node]) if node in adj_list else []
    adj_nodes.sort() # Small number first
    for adj_node in adj_nodes:
        if not bfs_visited[adj_node - 1]:
            bfs_visited[adj_node - 1] = True
            bfs_queue.append(adj_node)

print(' '.join(bfs_path))
