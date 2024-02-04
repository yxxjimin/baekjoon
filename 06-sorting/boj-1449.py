num_holes, tape_length = map(int, input().split())

holes = list(map(int, input().split()))
holes.sort()

tapes_count = 0
remaining_length = 0
prev_hole = -1
for hole in holes:
    remaining_length -= (hole - prev_hole)
    if remaining_length < 0:
        tapes_count += 1
        remaining_length = tape_length - 1
    prev_hole = hole

print(tapes_count)
