num_computers = int(input())
num_edges = int(input())

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
visited = [False] * num_computers
dfs_stack = [1]
while len(dfs_stack) > 0:
    node = dfs_stack.pop()
    if not visited[node - 1]:
        visited[node - 1] = True
        # Handle num_edges = 0 (Empty adjacency list)
        adj_nodes = adj_list[node] if node in adj_list else []
        for adj_node in adj_nodes:
            if not visited[adj_node - 1]:
                dfs_stack.append(adj_node)

print(sum(visited[1:]))
