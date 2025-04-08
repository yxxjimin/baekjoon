import sys


DIRECTIONS = {
    1: (-1, 0), 2: (-1, -1), 3: (0, -1), 4: (1, -1),
    5: (1, 0), 6: (1, 1), 7: (0, 1), 8: (-1, 1),
}


class GridState:
    shark: tuple[int, int, int]
    fishes: dict[int, tuple[int, int, int]]
    grid: list[list[int]]

    def __init__(self, shark: tuple, fishes: dict):
        self.shark = shark
        self.fishes = fishes.copy()
        self.grid = [[-1 for _ in range(4)] for _ in range(4)]
        for fish, (row, col, _) in self.fishes.items():
            self.grid[row][col] = fish

    def _eat_fish(self):
        row, col, _ = self.shark
        fish = self.grid[row][col]
        self.fishes.pop(fish)
        self.grid[row][col] = -1

    def _fish_movable(self, row: int, col: int) -> bool:
        row_shark, col_shark, _ = self.shark
        return (
            0 <= row < 4 and 0 <= col < 4 
            and not (row == row_shark and col == col_shark)
        )
    
    def _move_fish(self, fish: int, tgt_r: int, tgt_c: int):
        src_r, src_c, src_d = self.fishes[fish]
        tgt_fish = self.grid[tgt_r][tgt_c]
        self.grid[src_r][src_c], self.grid[tgt_r][tgt_c] = (
            self.grid[tgt_r][tgt_c],
            self.grid[src_r][src_c]
        )
        self.fishes[fish] = (tgt_r, tgt_c, src_d)
        if tgt_fish > 0:
            _, _, tgt_d = self.fishes[tgt_fish]
            self.fishes[tgt_fish] = (src_r, src_c, tgt_d)
            
    def _move_fishes(self):
        for fish in sorted(self.fishes.keys()):
            row, col, dir = self.fishes[fish]
            for i in range(9):
                new_dir = (dir + i - 1) % 8 + 1 
                dy, dx = DIRECTIONS[new_dir]
                if self._fish_movable(row + dy, col + dx):
                    self.fishes[fish] = (row, col, new_dir)
                    self._move_fish(fish, row + dy, col + dx)
                    break

    def _next_shark_moves(self) -> list[tuple[int, int, int]]:
        row, col, dir = self.shark
        dy, dx = DIRECTIONS[dir]
        return [
            self.fishes[self.grid[n_row][n_col]]
            for i in range(1, 4)
            if (
                0 <= (n_row := row + i * dy) < 4 
                and 0 <= (n_col := col + i * dx) < 4 
                and self.grid[n_row][n_col] > 0
            )
        ]

    def get_next_moves(self) -> list[tuple[int, int, int]]:
        self._eat_fish()
        self._move_fishes()
        return self._next_shark_moves()
    
    def get_points(self) -> int:
        return 136 - sum(self.fishes)


def _get_initial_state() -> GridState:
    fishes = dict()
    for i in range(4):
        line = list(map(int, sys.stdin.readline().split()))
        for j in range(4):
            fish_num, fish_dir = line[2 * j], line[2 * j + 1]
            fishes[fish_num] = (i, j, fish_dir)
            if i | j == 0:
                shark = (i, j, fish_dir)
    return GridState(shark, fishes)


def main():
    max_points = 0
    stack: list[GridState] = [_get_initial_state()]

    while len(stack) > 0:
        state = stack.pop()
        next_moves = state.get_next_moves()
        if len(next_moves) == 0:
            max_points = max(max_points, state.get_points())
        else:
            for move in next_moves:
                stack.append(GridState(move, state.fishes))

    print(max_points)


if __name__ == "__main__":
    main()
