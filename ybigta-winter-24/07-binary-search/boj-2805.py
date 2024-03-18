import sys

_, target_sum = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))

def search(tgt_sum: int) -> int:
    lo, hi = 0, int(1e9)
    while lo < hi:
        mid = (lo + hi) // 2

        cur_sum = 0
        for tree in trees:
            if tree > mid:
                cur_sum += tree - mid

        # Bisect right
        if tgt_sum > cur_sum:
            hi = mid
        else:
            lo = mid + 1

    return lo - 1

print(search(target_sum))
