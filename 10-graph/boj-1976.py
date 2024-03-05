import sys


def find(s: list, p: int) -> int:
    x = p
    while s[x] != x:
        x = s[x]
    s[p] = x

    return s[p]


def union(s: list, p: int, q: int) -> list:
    p_root = find(s, p)
    q_root = find(s, q)

    if p_root != q_root:
        s[q_root] = p_root

    return s


def main():
    num_vertex = int(sys.stdin.readline())
    _ = sys.stdin.readline()
    parent = [i for i in range(num_vertex + 1)]

    for i in range(num_vertex):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(i):
            if row[j] == 1:
                union(parent, i + 1, j + 1)

    path = list(map(int, sys.stdin.readline().split()))
    root = find(parent, path[0])

    valid = True
    for v in path:
        if find(parent, v) != root:
            valid = False
            break
    
    print("YES" if valid else "NO")


if __name__ == "__main__":
    main()
    