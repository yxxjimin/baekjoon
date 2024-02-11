import sys, bisect


def main() -> int:
    _, num_disc = map(int, input().split())
    lectures = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(lectures)):
        lectures[i] += lectures[i - 1]

    lo, hi = 1, int(1e9)

    while lo < hi:
        mid = (lo + hi) // 2
        
        if not fillable(lectures, num_disc, mid):
            lo = mid + 1
        else:
            hi = mid

    return lo


def fillable(sum_list: list, num_disc: int, disc_size: int) -> bool:
    sum = 0
    for _ in range(num_disc):
        sum = sum_list[bisect.bisect_right(sum_list, sum + disc_size) - 1]
        if sum == sum_list[-1]:
            return True
    
    return False


if __name__ == "__main__":
    print(main())
