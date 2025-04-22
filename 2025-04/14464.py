import bisect
import sys


def main():
    c, n = map(int, sys.stdin.readline().split())
    chickens = [int(sys.stdin.readline()) for _ in range(c)]
    cows = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    chickens.sort()
    cows.sort(key=lambda x: (x[1], x[0]))
    
    cnt = 0

    for start, end in cows:
        loc = bisect.bisect_left(chickens, start)
        if loc < len(chickens) and chickens[loc] <= end:
            cnt += 1
            chickens.pop(loc)
    
    print(cnt)


if __name__ == "__main__":
    main()
