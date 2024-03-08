import sys


def union(s: list, p: int, q: int) -> bool:

    def find(p: int) -> int:
        if p == s[p]:
            return s[p]
        s[p] = find(s[p])

        return s[p]
    
    p_root = find(p)
    q_root = find(q)

    if p_root != q_root:
        s[q_root] = p_root
        return True
    
    return False


def main():
    row, col = map(int, sys.stdin.readline().split())
    parent = [i for i in range(row * col)]
    
    def next_vertex(r: int, c: int, d: str) -> int:
        if d == 'U':
            return (r - 1) * col + c
        elif d == 'D':
            return (r + 1) * col + c
        elif d == 'L':
            return r * col + (c - 1)
        elif d == 'R':
            return r * col + (c + 1)
        return -1

    count = 0
    for r in range(row):
        line = sys.stdin.readline().strip()
        for c in range(col):
            if not union(parent, r * col + c, next_vertex(r, c, line[c])):
                count += 1
            
    print(count)


if __name__ == "__main__":
    main()
