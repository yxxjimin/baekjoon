"""
문제 : https://www.acmicpc.net/problem/14719
날짜 : 24/04/04

- 현재 위치에 물이 고일 수 있는 지 완전 탐색
- 현재 위치를 기준으로 왼쪽, 오른쪽 벽의 높이를 탐색
"""

import sys


def main():
    _ = sys.stdin.readline()
    heights = list(map(int, sys.stdin.readline().split()))

    answer = 0

    for i in range(1, len(heights) - 1):
        left_wall = max(heights[:i])
        right_wall = max(heights[i + 1:])
        wall_height = min(left_wall, right_wall)

        if heights[i] < wall_height:
            answer += wall_height - heights[i]
    
    print(answer)


if __name__ == "__main__":
    main()
