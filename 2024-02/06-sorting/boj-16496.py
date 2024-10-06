import sys

n = int(input())

# If A + B > B + A: [A, B]
# If A + B < B + A: [B, A]
# => Compare A + B and A + A to sort A & B
numbers = list(sys.stdin.readline().split())
numbers.sort(
    key=lambda s: (s * (10 // len(s) + 1))[:10],
    reverse=True)

answer = ''.join(numbers)
print(int(answer))
