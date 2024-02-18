import sys


def main():
    num_mat = int(sys.stdin.readline())

    # Size of i^th matrix: seq[i - 1] * seq[i]
    seq = []
    for _ in range(num_mat):
        row, col = map(int, sys.stdin.readline().split())
        seq.append(row)
    seq.append(col)

    dp_table = [[0] * (num_mat + 1) for _ in range(num_mat + 1)]

    # A_i ... A_j = (A_i ... A_k) * (A_k+1 ... A_j)
    for length in range(2, num_mat + 1):
        for i in range(1, num_mat - length + 2):
            j = i + length - 1
            dp_table[i][j] = min([dp_table[i][k] 
                                  + dp_table[k + 1][j] 
                                  + seq[i - 1] * seq[k] * seq[j] 
                                  for k in range(i, j)])

    print(dp_table[1][num_mat])
    

if __name__ == "__main__":
    main()
