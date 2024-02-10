# ┌─────────────────────────┐
# │ [A] Set                 │
# │   - Memory :  47,448 KB │
# │   - Time   :     148 ms │
# └─────────────────────────┘
import sys

_ = input()
numbers = set(map(int, sys.stdin.readline().split()))

_ = input()
targets = map(int, sys.stdin.readline().split())
answers = [1 if tgt in numbers else 0 for tgt in targets]
print(*answers, sep='\n')


# ┌─────────────────────────┐
# │ [B] `bisect_left()`     │
# │   - Memory :  46,396 KB │
# │   - Time   :     244 ms │
# └─────────────────────────┘
import sys, bisect

_ = input()
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

_ = input()
targets = map(int, sys.stdin.readline().split())

def number_exists(target: int) -> int:
    idx = bisect.bisect_left(numbers, target)
    if idx < len(numbers) and numbers[idx] == target:
        return 1
    return 0

answers = [number_exists(tgt) for tgt in targets]
print(*answers, sep='\n')


# ┌─────────────────────────┐
# │ [C] Binary Search       │
# │   - Memory :  44,336 KB │
# │   - Time   :     400 ms │
# └─────────────────────────┘
import sys

_ = input()
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

def number_exists(target: int) -> int:
    start, end = 0, len(numbers)
    while start < end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            return 1
        elif numbers[mid] < target:
            start = mid + 1
        else:
            end = mid
    return 0

_ = input()
targets = map(int, sys.stdin.readline().split())
answers = [number_exists(tgt) for tgt in targets]
print(*answers, sep='\n')
