"""
Runtime : 52 ms
Memory  : 33.432 MB
"""
import sys


def find(p: int, parent: list[int]) -> int:
    if p != parent[p]:
        parent[p] = find(parent[p], parent)
    return parent[p]


def union(p: int, q: int, parent: list[int]):
    p_root = find(p, parent)
    q_root = find(q, parent)

    if p_root != q_root:
        parent[q_root] = p_root


def red_or_green(x: str, y: str) -> bool:
    return x == y or x != "B" and y != "B"


def solution():
    n = int(sys.stdin.readline())
    grid = [list(sys.stdin.readline().strip()) for _ in range(n)]
    parent = [i for i in range(n * n)]
    parent_rg = [i for i in range(n * n)]
    dydx = [(0, 1), (1, 0)]

    for i in range(n):
        for j in range(n):
            for dy, dx in dydx:
                ni, nj = i + dy, j + dx
                if ni < n and nj < n:
                    if grid[i][j] == grid[ni][nj]:
                        union(i * n + j, ni * n + nj, parent)
                    if red_or_green(grid[i][j], grid[ni][nj]):
                        union(i * n + j, ni * n + nj, parent_rg)
    
    print(
        len(set([find(i, parent) for i in range(n * n)])),
        len(set([find(i, parent_rg) for i in range(n * n)]))
    )
    

if __name__ == "__main__":
    solution()
