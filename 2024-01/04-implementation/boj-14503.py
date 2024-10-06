# Read input
n, m = map(int, input().split())
curr_r, curr_c, curr_dir = map(int, input().split())

# 0: Not cleaned, 1: Wall, 2: Cleaned
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
get_room = lambda loc: room[loc[0]][loc[1]]
move_by = lambda dir: (curr_r + move[dir][0], curr_c + move[dir][1])

# Move the robot
cleaned_count = 0
not_moved = 0
while True:
    # (1) Clean current tile
    if get_room((curr_r, curr_c)) == 0:
        room[curr_r][curr_c] = 2
        cleaned_count += 1

    # (2) If all adjacent tiles cleaned
    if not_moved == 4:
        back_dir = (curr_dir + 2) % 4
        # if room[curr_r + move[back_dir][0]][curr_c + move[back_dir][1]] == 1:
        if get_room(move_by(back_dir)) == 1:
            break
        else:
            curr_r, curr_c = move_by(back_dir)
            not_moved = 0
    
    # (3) Clean adjacent tile
    curr_dir = (curr_dir + 3) % 4
    if get_room(move_by(curr_dir)) == 0:
        curr_r, curr_c = move_by(curr_dir)
        not_moved = 0
    else:
        not_moved += 1

print(cleaned_count)
