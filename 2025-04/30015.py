import sys


def filter_by_digit(nums: list[int], digit: int) -> list[int]:
    return [num for num in nums if num & (1 << digit)]


def main():
    _, k = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    score = 0

    for i in range(21):
        filtered = filter_by_digit(nums, 20 - i)
        if len(filtered) >= k:
            nums = filtered
            score |= 1 << (20 - i)

    print(score)


if __name__ == "__main__":
    main()
