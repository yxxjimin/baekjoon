import sys


def is_available(size: int, grid: list[list[int]], row: int, col: int) -> bool:
    return (
        row + size <= 10 
        and col + size <= 10 
        and sum([sum(grid[row + i][col : col + size]) for i in range(size)]) 
        == size**2
    )


def get_maximum_size(
    grid: list[list[int]], row: int, col: int, papers: dict[int, int]
) -> int:
    for size in range(5, 0, -1):
        if is_available(size, grid, row, col) and papers[size] > 0:
            return size
    return 0


def backtrack(loc: int, grid: list[list[int]], papers: dict[int, int]) -> int:
    if loc == 100:
        return 25 - sum(papers.values())
    
    row, col = divmod(loc, 10)
    if grid[row][col] < 1:
        return backtrack(loc + 1, grid, papers)
    
    cnt = 26
    for size in range(get_maximum_size(grid, row, col, papers), 0, -1):
        if papers[size] > 0:
            for i in range(row, row + size):
                grid[i][col : col + size] = [-1 for _ in range(size)]
            papers[size] -= 1

            if (ret := backtrack(loc + 1, grid, papers)) > -1:
                cnt = min(cnt, ret)

            for i in range(row, row + size):
                grid[i][col : col + size] = [1 for _ in range(size)]
            papers[size] += 1

    return -1 if cnt > 25 else cnt


def main():
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
    papers = {i: 5 for i in range(1, 6)}
    print(backtrack(0, grid, papers))


if __name__ == "__main__":
    main()
