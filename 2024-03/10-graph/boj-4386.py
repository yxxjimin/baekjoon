import sys, math, itertools


def get_distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def kruskal(e: list, n: int) -> float:
    parent = [i for i in range(n)]


    def find(u: int) -> int:
        x = u
        while parent[x] != x:
            x = parent[x]
        parent[u] = x

        return parent[u]


    def union(p: int, q: int) -> bool:
        p_root = find(p)
        q_root = find(q)

        if p_root != q_root:
            parent[q_root] = p_root
            return True

        return False


    weight_sum = 0
    for u, v, w in e:
        if union(u, v):
            weight_sum += w

    return weight_sum


def main():
    num_vertex = int(sys.stdin.readline())
    loc = dict()

    # Read locations
    for i in range(num_vertex):
        x, y = map(float, sys.stdin.readline().split())
        loc[i] = (x, y)

    # Construct all edges
    edges = []
    for u, v in itertools.combinations(range(num_vertex), 2):
        edges.append((u, v, get_distance(loc[u], loc[v])))
    edges.sort(key=lambda x: x[2])
    
    # MST
    answer = kruskal(edges, num_vertex)
    print(f"{answer:.2f}")


if __name__ == "__main__":
    main()
