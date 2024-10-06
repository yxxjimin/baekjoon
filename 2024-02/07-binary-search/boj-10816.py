# ┌─────────────────────────┐
# │ [A] Dictionary          │
# │   - Memory : 162,200 KB │
# │   - Time   :     864 ms │
# └─────────────────────────┘
import sys
from collections import defaultdict

_ = input()
cards = defaultdict(int)
for number in map(int, sys.stdin.readline().split()):
    cards[number] += 1

_ = input()
answers = [cards[tgt] for tgt in map(int, sys.stdin.readline().split())]
print(*answers)


# ┌─────────────────────────┐
# │ [B] `bisect()`          │
# │   - Memory : 116,432 KB │
# │   - Time   :   1,356 ms │
# └─────────────────────────┘
import sys, bisect

_ = input()
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

def count_cards(target: int) -> int:
    lo = bisect.bisect_left(cards, target)
    hi = bisect.bisect_right(cards, target)
    
    return hi - lo

_ = input()
answers = [count_cards(tgt) for tgt in map(int, sys.stdin.readline().split())]
print(*answers)
