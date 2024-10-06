# Read input
n, m, curr_r, curr_c, cmd_count = map(int, input().split())

map_ = []
for _ in range(n):
    map_.append(list(map(int, input().split())))
cmd = list(map(int, input().split()))

# Tile utils
move = [(0, 1), (0, -1), (-1, 0), (1, 0)] # E W N S
get_tile = lambda loc: map_[loc[0]][loc[1]]
move_by = lambda dir: (curr_r + move[dir - 1][0], curr_c + move[dir - 1][1])
within_map_range = lambda loc: loc[0] in range(n) and loc[1] in range(m)

def set_current_tile(val):
    map_[curr_r][curr_c] = val

# Dice utils
#
#     (N)
# (W) (B) (E)
#     (S)
#    (5-B)
dice = [0, 0, 0, 0, 0, 0]
current_bottom = 0
ewns_faces = [2, 3, 4, 1]

def roll_dice_to(dir):
    global curr_r
    global curr_c
    global current_bottom

    curr_r, curr_c = move_by(dir)

    new_bottom = ewns_faces[dir - 1]
    if dir == 1:
        ewns_faces[0] = 5 - current_bottom
        ewns_faces[1] = current_bottom
    elif dir == 2:
        ewns_faces[0] = current_bottom
        ewns_faces[1] = 5 - current_bottom
    elif dir == 3:
        ewns_faces[2] = 5 - current_bottom
        ewns_faces[3] = current_bottom
    else:
        ewns_faces[2] = current_bottom
        ewns_faces[3] = 5 - current_bottom
    current_bottom = new_bottom

# Execute commands
for dir in cmd:
    # Move within map range
    if within_map_range(move_by(dir)):
        roll_dice_to(dir)

        # Change bottom face number
        if get_tile((curr_r, curr_c)) == 0:
            set_current_tile(dice[current_bottom])
        else:
            dice[current_bottom] = get_tile((curr_r, curr_c))
            set_current_tile(0)
        
        # Print top face number
        print(dice[5 - current_bottom])
