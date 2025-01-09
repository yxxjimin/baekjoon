import sys


def solve():
    pw_len = int(sys.stdin.readline())
    answer_pw = sys.stdin.readline().strip()

    cnt = 0
    for i in range(len(answer_pw)):
        digit_diff = ord(answer_pw[i]) - ord("a")
        cnt += digit_diff * sum([26 ** k for k in range(pw_len - i)]) + 1

    print(cnt)


if __name__ == "__main__":
    solve()
