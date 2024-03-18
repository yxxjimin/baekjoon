import sys

num_cables, cables_needed = map(int, input().split())
cables = [int(sys.stdin.readline()) for _ in range(num_cables)]

def search(tgt_cables: int) -> int:
    # 리턴 값이 (상한 - 1) 이므로 2^31 - 1이 아니라 2^31로 설정
    lo, hi = 1, 2 ** 31

    while lo < hi:
        mid = (lo + hi) // 2

        cur_cables = 0
        for cable in cables:
            cur_cables += cable // mid
        
        # Upper bound
        if cur_cables < tgt_cables:
            hi = mid
        else:
            lo = mid + 1

    return lo - 1

print(search(cables_needed))
