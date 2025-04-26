import math
import sys


def solve(tgt: int):
    for i in range(2, int(math.sqrt(2 * tgt)) + 1):
        total_offset = tgt - i * (i + 1) // 2
        if total_offset % i == 0:
            offset = total_offset // i + 1
            lo, hi = offset, offset + i
            print(f"{tgt} = {' + '.join([str(i) for i in range(lo, hi)])}")
            return
    print("IMPOSSIBLE")


def main():
    for _ in range(int(sys.stdin.readline())):
        solve(int(sys.stdin.readline()))


if __name__ == "__main__":
    main()
