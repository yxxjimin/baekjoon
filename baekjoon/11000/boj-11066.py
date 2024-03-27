import sys


def main():
    _ = sys.stdin.readline()
    books = list(map(int, sys.stdin.readline().split()))
    dp_table = [[0] * len(books) for _ in range(len(books))]

    book_sums = [0] * (len(books) + 1)
    book_sums[0] = books[0]
    for i in range(1, len(books)):
        book_sums[i] = book_sums[i - 1] + books[i]

    for l in range(1, len(books)):
        for i in range(len(books) - l):
            j = i + l
            curr_sum = book_sums[j] - book_sums[i - 1]
            dp_table[i][j] = min(
                [dp_table[i][k] + dp_table[k + 1][j] + curr_sum
                 for k in range(i, j)]
            )

    print(dp_table[0][-1])


if __name__ == "__main__":
    for _ in range(int(sys.stdin.readline())):
        main()
