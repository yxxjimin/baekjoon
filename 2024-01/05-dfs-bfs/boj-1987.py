r, c = map(int, input().split())

board = [list(map(lambda ch: ord(ch) - 65, input())) for _ in range(r)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited_alphabet = [False] * 26
max_length = 1

def dfs(row: int, col: int, curr_len: int):
    global max_length
    # End of path
    if visited_alphabet[board[row][col]]:
        max_length = max(max_length, curr_len - 1)
        return
    
    # DFS
    visited_alphabet[board[row][col]] = True
    for dy, dx in dir:
        if row + dy in range(r) and col + dx in range(c):
            dfs(row + dy, col + dx, curr_len + 1)
    visited_alphabet[board[row][col]] = False

dfs(0, 0, 1)
print(max_length)
