import sys


def main():
    """
    ┌─────────────────────────┐
    │ [A] 2 Rows only         │
    │   - Memory :  31,120 KB │
    │   - Time   :     456 ms │
    └─────────────────────────┘
    """
    row, col = map(int, sys.stdin.readline().split())
    
    # Need only current & previous rows, not the whole N*N table
    prev_row_dp = [0] * (col + 1)
    
    # Zero-padding on top & left
    for _ in range(row):
        curr_row_dp = [0] + list(map(int, sys.stdin.readline().split()))

        # DP 테이블 값이 우측/하단의 사탕 개수과 무관하므로 이 시점에 미리 계산해도 무방
        for c in range(1, col + 1):
            curr_row_dp[c] += max(curr_row_dp[c - 1], 
                                  prev_row_dp[c - 1], 
                                  prev_row_dp[c])
        
        prev_row_dp = curr_row_dp
    
    print(curr_row_dp[col])


def main2():
    """
    ┌─────────────────────────┐
    │ [B] N * N DP Table      │
    │   - Memory :  70,048 KB │
    │   - Time   :     544 ms │
    └─────────────────────────┘
    """
    row, col = map(int, sys.stdin.readline().split())
    dp_table = [[0] * (col + 1) for _ in range(row + 1)]
    
    # Zero-padding on top & left
    for r in range(1, row + 1):
        dp_table[r][1:] = list(map(int, sys.stdin.readline().split()))

        # DP 테이블 값이 우측/하단의 사탕 개수과 무관하므로 이 시점에 미리 계산해도 무방
        for c in range(1, col + 1):
            dp_table[r][c] += max(dp_table[r - 1][c], 
                                  dp_table[r][c - 1], 
                                  dp_table[r - 1][c - 1])
    
    print(dp_table[row][col])


if __name__ == "__main__":
    main()
 