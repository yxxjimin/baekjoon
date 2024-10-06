import sys


def find(s: list, p: int) -> int:
    if s[p] != p:
        s[p] = find(s, s[p])
    
    return s[p]


def union(s: list, p: int, q: int) -> list:
    p_root = find(s, p)
    q_root = find(s, q)

    if p_root != q_root:
        s[q_root] = p_root
        
    return s


def main():
    num_elem, num_operation = map(int, sys.stdin.readline().split())
    sets = [i for i in range(num_elem + 1)]

    for _ in range(num_operation):
        op, a, b = map(int, sys.stdin.readline().split())

        if op:
            print("YES" if find(sets, a) == find(sets, b) else "NO")
        else:
            sets = union(sets, a, b)


if __name__ == "__main__":
    main()
