import sys


def backtrack(cur: int, eggs: list[tuple[int, int]]) -> int:
    if cur == len(eggs):
        return sum([1 for dur, _ in eggs if dur <= 0])
    
    cur_dur, cur_wgt = eggs[cur]
    res, is_egg_hit = 0, False
    
    for egg, (dur, wgt) in enumerate(eggs):
        if cur_dur > 0 and egg != cur and dur > 0:
            eggs[cur][0] -= wgt
            eggs[egg][0] -= cur_wgt
            is_egg_hit = True
            res = max(res, backtrack(cur + 1, eggs))
            eggs[cur][0] += wgt
            eggs[egg][0] += cur_wgt

    if not is_egg_hit:
        res = backtrack(cur + 1, eggs)
        
    return res


def main():
    n = int(sys.stdin.readline())
    eggs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(backtrack(0, eggs))


if __name__ == "__main__":
    main()
