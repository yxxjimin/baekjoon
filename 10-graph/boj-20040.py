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


def main():
    num_vertex, num_edge = map(int, sys.stdin.readline().split())
    parent = [i for i in range(num_vertex)]

    answer = 0

    for i in range(num_edge):
        src, dst = map(int, sys.stdin.readline().split())
        src_root = find(parent, src)
        dst_root = find(parent, dst)

        if src_root == dst_root:
            answer = i + 1
            break
        else:
            union(parent, src_root, dst_root)

    print(answer)


if __name__ == "__main__":
    main()
