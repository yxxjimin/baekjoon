"""
문제 : https://www.acmicpc.net/problem/3055
날짜 : 24/04/11

- 물 먼저 BFS 돌린 다음 고슴도치 BFS 돌리면 해결
"""

import sys
from collections import deque


def main():
    height, width = map(int, sys.stdin.readline().split())
    drdc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    graph = [[] for _ in range(height)]
    
    hdghg_queue = deque()
    water_queue = deque()

    for r in range(height):
        line = sys.stdin.readline().strip()
        for c in range(width):
            graph[r].append(line[c])

            if line[c] == "S":
                hdghg_queue.append((r, c))
            elif line[c] == "*":
                water_queue.append((r, c))
            elif line[c] == "D":
                tgt = (r, c)
    
    # BFS
    time = 0
    while hdghg_queue:
        time += 1
        
        # Water flows
        for _ in range(len(water_queue)):
            curr_r, curr_c = water_queue.popleft()
            for dr, dc in drdc:
                new_r = curr_r + dr
                new_c = curr_c + dc
                if (new_r in range(height) 
                    and new_c in range(width) 
                    and (graph[new_r][new_c] == "."
                         or graph[new_r][new_c] == "S")):
                    
                    graph[new_r][new_c] = "*"
                    water_queue.append((new_r, new_c))

        # Hedgehg moves
        for _ in range(len(hdghg_queue)):
            curr_r, curr_c = hdghg_queue.popleft()
            for dr, dc in drdc:
                new_r = curr_r + dr
                new_c = curr_c + dc

                if (new_r in range(height) and new_c in range(width)):
                    
                    # Arrived
                    if graph[new_r][new_c] == "D":
                        print(time)
                        return
                    
                    elif graph[new_r][new_c] == ".":
                        graph[new_r][new_c] = "S"
                        hdghg_queue.append((new_r, new_c))
            
    print("KAKTUS")


if __name__ == "__main__":
    main()
