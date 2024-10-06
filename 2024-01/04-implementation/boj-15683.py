import sys
sys.setrecursionlimit(50000)

n, m = map(int, input().split())

cctv_directions = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

dydx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

office = [list(map(int, input().split())) for _ in range(n)]

def investigate(r: int, c: int, directions: list) -> set:
    # Return a set of watched points on current rotation
    watched = set()
    watched.add((r, c))
    for dir in directions:
        new_r = r
        new_c = c
        while True:
            new_r += dydx[dir][0]
            new_c += dydx[dir][1]
            if (new_r not in range(n) 
                or new_c not in range(m)
                or office[new_r][new_c] == 6):
                break
            else:
                watched.add((new_r, new_c))

    return watched

cctvs = []
init_watched = set()
for r in range(n):
    for c in range(m):
        if office[r][c] in range(1, 6):
            cctv_type = office[r][c]
            cctvs.append(
                [investigate(r, c, dir) for dir in cctv_directions[cctv_type]]
            )
        elif office[r][c] == 6:
            # Walls are not blind spots
            init_watched.add((r, c))

blind_spots = m * n

def dfs(cctv_idx: int, prev_watched: set):
    # Search finished, count blind spots
    global blind_spots
    if cctv_idx == len(cctvs):
        blind_spots = min(blind_spots, m * n - len(prev_watched))
        return

    # DFS for each rotations
    for watched_set in cctvs[cctv_idx]:
        current_watched = prev_watched.union(watched_set)
        dfs(cctv_idx + 1, current_watched)

dfs(0, init_watched)
print(blind_spots)
