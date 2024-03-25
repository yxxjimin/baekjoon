import sys


def main():
    num_phones = int(sys.stdin.readline())

    # Shorter strings should be considered first
    phones = [sys.stdin.readline().strip() for _ in range(num_phones)]
    phones.sort()

    consistent = True

    for i in range(1, len(phones)):
        if phones[i - 1] == phones[i][:len(phones[i - 1])]:
            consistent = False
            break

    print("YES" if consistent else "NO")


if __name__ == "__main__":
    for _ in range(int(sys.stdin.readline())):
        main()
