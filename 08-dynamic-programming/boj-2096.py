import sys


def main():
    n = int(sys.stdin.readline())

    prev_l_max, prev_c_max, prev_r_max = 0, 0, 0
    prev_l_min, prev_c_min, prev_r_min = 0, 0, 0
    for _ in range(n):
        curr_l, curr_c, curr_r = map(int, sys.stdin.readline().split())

        curr_l_max = curr_l + max(prev_l_max, prev_c_max)
        curr_c_max = curr_c + max(prev_l_max, prev_c_max, prev_r_max)
        curr_r_max = curr_r + max(prev_c_max, prev_r_max)

        curr_l_min = curr_l + min(prev_l_min, prev_c_min)
        curr_c_min = curr_c + min(prev_l_min, prev_c_min, prev_r_min)
        curr_r_min = curr_r + min(prev_c_min, prev_r_min)

        prev_l_max, prev_c_max, prev_r_max = curr_l_max, curr_c_max, curr_r_max
        prev_l_min, prev_c_min, prev_r_min = curr_l_min, curr_c_min, curr_r_min

    print(max(curr_l_max, curr_c_max, curr_r_max), 
          min(curr_l_min, curr_c_min, curr_r_min))


if __name__ == "__main__":
    main()
