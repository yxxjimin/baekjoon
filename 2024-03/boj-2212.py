"""
문제 : https://www.acmicpc.net/problem/2212
날짜 : 24/03/28

- 센서 위치를 정렬한 다음 N개의 센서를 K개의 파티션으로 분할
- 인접한 애들끼리 거리를 다 구해서 거리가 가장 먼 애들을 기준으로 분할하면 된다(그리디).
"""

import sys


def main():
    _ = sys.stdin.readline()
    num_parts = int(sys.stdin.readline())
    locations = list(map(int, sys.stdin.readline().split()))
    locations.sort()

    gap = [locations[i] - locations[i - 1] for i in range(1, len(locations))]
    gap.sort()
    
    answer = 0
    if gap:
        answer = sum(gap[:len(locations) - num_parts])
    
    print(answer)


if __name__ == "__main__":
    main()
