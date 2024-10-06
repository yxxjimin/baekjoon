"""
문제 : https://www.acmicpc.net/problem/17144
날짜 : 24/04/08

- 그냥 주어진대로 구현하기
- 파이썬 쓰면 시간 초과, PyPy3 쓰면 통과
"""

import sys


def spread(g: list[list[int]]) -> list[list[int]]:
    new_g = [[0] * col for _ in range(row)]
    dydx = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for r in range(row):
        for c in range(col):
            if g[r][c] > 0:
                spread_amount = int(g[r][c] / 5)
                count = 0
                
                for dy, dx in dydx:
                    new_r, new_c = r + dy, c + dx
                    if (new_r in range(row) 
                        and new_c in range(col) 
                        and g[new_r][new_c] != -1):
                        
                        new_g[new_r][new_c] += spread_amount
                        count += 1
                        
                new_g[r][c] += g[r][c] - spread_amount * count
            else:
                new_g[r][c] += g[r][c]
    
    return new_g


def purify(g: list[list[int]]) -> list[list[int]]:
    new_g = [[g[r][c] for c in range(col)] for r in range(row)]

    pur_1 = [r[0] for r in g].index(-1)
    pur_2 = pur_1 + 1

    for c in range(1, col):
        # Right
        new_g[pur_1][c] = g[pur_1][c - 1] if c > 1 else 0
        new_g[pur_2][c] = g[pur_2][c - 1] if c > 1 else 0

        # Left
        new_g[0][c - 1] = g[0][c]
        new_g[row - 1][c - 1] = g[row - 1][c]

    # Up / Down
    for r in range(pur_1):
        new_g[r][col - 1] = g[r + 1][col - 1]
        new_g[r + 1][0] = g[r][0]
    
    for r in range(pur_2, row - 1):
        new_g[r + 1][col - 1] = g[r][col - 1]
        new_g[r][0] = g[r + 1][0]

    new_g[pur_1][0] = -1
    new_g[pur_2][0] = -1

    return new_g


if __name__ == "__main__":
    row, col, time = map(int, sys.stdin.readline().split())
    room = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

    for _ in range(time):
        room = purify(spread(room))
    
    answer = sum([sum(room[i]) for i in range(row)]) + 2
    print(answer)
    