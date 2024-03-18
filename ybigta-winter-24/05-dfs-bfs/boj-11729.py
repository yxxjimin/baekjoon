count = 0
moves = []
def move_tower(height: int, src: int, tgt: int):
    global count
    if height == 1:
        count += 1
        moves.append(f"{src} {tgt}")
        return

    aux = 6 - src - tgt
    move_tower(height - 1, src, aux)
    count += 1
    moves.append(f"{src} {tgt}")
    move_tower(height - 1, aux, tgt)

n = int(input())
move_tower(n, 1, 3)
print(count)
for line in moves:
    print(line)
