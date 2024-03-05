import sys


def find(s: list, p: int) -> int:
    x = p
    while s[x] != x:
        x = s[x]
    s[p] = x

    return s[p]


def union(s: list, p: int, q: int) -> bool:
    p_root = find(s, p)
    q_root = find(s, q)

    if p_root != q_root:
        s[q_root] = p_root
        return True

    return False


def main():
    num_vertex = int(sys.stdin.readline())
    num_edge = int(sys.stdin.readline())
    parent = [i for i in range(num_vertex + 1)]
    edges = []

    for _ in range(num_edge):
        edges.append(tuple(map(int, sys.stdin.readline().split())))
    edges.sort(key=lambda x: x[2])

    weight_sum = 0
    for u, v, w in edges:
        if union(parent, u, v):
            weight_sum += w

    print(weight_sum)


if __name__ == "__main__":
    main()
