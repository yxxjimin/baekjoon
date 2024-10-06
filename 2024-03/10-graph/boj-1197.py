import sys


def find(s: list, p: int) -> int:
    x = p
    while s[x] != x:
        x = s[x]
    s[p] = x

    return s[p]


def union(s: list, p_root: int, q_root: int) -> list:
    if p_root != q_root:
        s[q_root] = p_root

    return s


def kruskal(e: list, s: list) -> int:
    e.sort(key=lambda x: x[2])
    weight_sum = 0

    for u, v, w in e:
        u_root = find(s, u)
        v_root = find(s, v)

        if u_root != v_root:
            union(s, u_root, v_root)
            weight_sum += w

    return weight_sum


def main():
    num_vertex, num_edge = map(int, sys.stdin.readline().split())
    parent = [i for i in range(num_vertex + 1)]
    edges = []

    for _ in range(num_edge):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w))

    answer = kruskal(edges, parent)

    print(answer)


if __name__ == "__main__":
    main()
    