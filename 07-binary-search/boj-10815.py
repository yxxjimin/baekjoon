# ┌─────────────────────────┐
# │ [A] Set                 │
# │   - Memory : 109,808 KB │
# │   - Time   :     560 ms │
# └─────────────────────────┘
import sys

n = int(input())
existing_cards = set(map(int, sys.stdin.readline().split()))

m = int(input())
search_targets = map(int, sys.stdin.readline().split())
answer = [1 if tgt in existing_cards else 0 for tgt in search_targets]
print(*answer)


# ┌─────────────────────────┐
# │ [B] Binary Search       │
# │   - Memory :  96,492 KB │
# │   - Time   :   1,804 ms │
# └─────────────────────────┘
import sys

n = int(input())
existing_cards = list(map(int, sys.stdin.readline().split()))
existing_cards.sort()

def number_exists(target: int) -> int:
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2

        if existing_cards[mid] == target:
            return 1
        elif existing_cards[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

m = int(input())
search_targets = map(int, sys.stdin.readline().split())
answer = list(map(number_exists, search_targets))
print(*answer)
