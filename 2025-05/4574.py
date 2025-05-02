import sys


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def str_to_loc(s: str) -> tuple[int, int]:
    return (ord(s[0]) - ord("A"), int(s[1]) - 1)


def get_box(row: int, col: int) -> int:
    return (row // 3) * 3 + col // 3


def place_num(
    num: int,
    grid: list[list[int]],
    row: int,
    col: int,
    row_used: list[set[int]],
    col_used: list[set[int]],
    box_used: list[set[int]],
):
    grid[row][col] = num
    row_used[row].add(num)
    col_used[col].add(num)
    box_used[get_box(row, col)].add(num)


def remove_num(
    num: int,
    grid: list[list[int]],
    row: int,
    col: int,
    row_used: list[set[int]],
    col_used: list[set[int]],
    box_used: list[set[int]],
):
    grid[row][col] = None
    row_used[row].remove(num)
    col_used[col].remove(num)
    box_used[get_box(row, col)].remove(num)


def is_sudoku_valid(
    num: int,
    row: int,
    col: int,
    row_used: list[set[int]],
    col_used: list[set[int]],
    box_used: list[set[int]],
) -> bool:
    return (
        num not in row_used[row]
        and num not in col_used[col]
        and num not in box_used[get_box(row, col)]
    )


def get_available_domino_locs(
    grid: list[list[int]], row: int, col: int
) -> list[tuple[int, int]]:
    return [
        (row + dy, col + dx)
        for dy, dx in DIRS
        if (
            0 <= row + dy < 9
            and 0 <= col + dx < 9
            and grid[row + dy][col + dx] is None
        )
    ]


def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row, sep="")


def backtrack(
    src: int,
    grid: list[list[int]],
    dominos: dict[tuple[int, int], bool],
    row_used: list[set[int]],
    col_used: list[set[int]],
    box_used: list[set[int]],
) -> bool:
    if src == 81:
        print_grid(grid)
        return True

    row, col = divmod(src, 9)

    if grid[row][col] is not None:
        return backtrack(src + 1, grid, dominos, row_used, col_used, box_used)

    for nrow, ncol in get_available_domino_locs(grid, row, col):
        for (u, v), used in dominos.items():
            if used:
                continue
            for a, b in [(u, v), (v, u)]:
                if is_sudoku_valid(
                    a, row, col, row_used, col_used, box_used
                ) and is_sudoku_valid(
                    b, nrow, ncol, row_used, col_used, box_used
                ):
                    place_num(a, grid, row, col, row_used, col_used, box_used)
                    place_num(b, grid, nrow, ncol, row_used, col_used, box_used)
                    dominos[(u, v)] = True

                    if backtrack(
                        src + 1, grid, dominos, row_used, col_used, box_used
                    ):
                        return True

                    dominos[(u, v)] = False
                    remove_num(a, grid, row, col, row_used, col_used, box_used)
                    remove_num(
                        b, grid, nrow, ncol, row_used, col_used, box_used
                    )
    return False


def solve(n: int):
    grid = [[None for _ in range(9)] for _ in range(9)]
    dominos = {(a, b): False for a in range(1, 10) for b in range(a + 1, 10)}

    row_used = [set() for _ in range(9)]
    col_used = [set() for _ in range(9)]
    box_used = [set() for _ in range(9)]

    for _ in range(n):
        num_u, pos_u, num_v, pos_v = sys.stdin.readline().split()
        num_u, num_v = int(num_u), int(num_v)
        row_u, col_u = str_to_loc(pos_u)
        row_v, col_v = str_to_loc(pos_v)

        place_num(num_u, grid, row_u, col_u, row_used, col_used, box_used)
        place_num(num_v, grid, row_v, col_v, row_used, col_used, box_used)
        dominos[(min(num_u, num_v), max(num_u, num_v))] = True

    for num, (row, col) in enumerate(
        map(str_to_loc, sys.stdin.readline().split())
    ):
        place_num(num + 1, grid, row, col, row_used, col_used, box_used)

    backtrack(0, grid, dominos, row_used, col_used, box_used)


def main():
    cnt = 1
    while (n := int(sys.stdin.readline())) > 0:
        print(f"Puzzle {cnt}")
        solve(n)
        cnt += 1


if __name__ == "__main__":
    main()
