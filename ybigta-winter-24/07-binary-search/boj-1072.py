# ┌─────────────────────────┐
# │ [A] Solve Algebra       │
# │   - Memory :  33,240 KB │
# │   - Time   :      44 ms │
# └─────────────────────────┘
import math

total_games, wins = map(int, input().split())
rate = int(100 * wins / total_games)

min_games = (math.ceil(((rate + 1) * total_games - 100 * wins) / (99 - rate))
             if rate < 99
             else -1)

print(min_games)


# ┌─────────────────────────┐
# │ [B] Parametric Search   │
# │   - Memory :  31,120 KB │
# │   - Time   :      44 ms │
# └─────────────────────────┘
import sys

total_games, wins = map(int, input().split())
threshold = int(100 * wins / total_games) + 1

def search() -> int:
    if threshold > 99:
        return -1

    lo, hi = 0, sys.maxsize
    
    # Find lower bound (Bisect left)
    while lo < hi:
        mid = (lo + hi) // 2
        win_rate = int(100 * (wins + mid) / (total_games + mid))
        
        if win_rate < threshold:
            lo = mid + 1
        else:
            hi = mid
        
    return lo

print(search())
