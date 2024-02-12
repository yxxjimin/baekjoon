import sys, bisect

num_houses, num_routers = map(int, input().split())
houses = [int(sys.stdin.readline()) for _ in range(num_houses)]
houses.sort()


def is_available(min_dist: int) -> bool:
    routers = [houses[0]]
    for i in range(num_routers - 1):
        loc = bisect.bisect_left(houses, routers[i] + min_dist)

        # Minimum distance is too long
        if loc == num_houses:
            return False
        routers.append(houses[loc])
        
    return True


def main():
    lo, hi = 1, int(1e9) + 1
    while lo < hi:
        mid = (lo + hi) // 2

        # Upper bound
        if not is_available(mid):
            hi = mid
        else:
            lo = mid + 1
    
    print(lo - 1)


if __name__ == "__main__":
    main()
