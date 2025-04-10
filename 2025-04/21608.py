import sys


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Grid:
    size: int
    seat: dict[int, tuple[int, int]] = dict()
    empty: list[list[int]]
    taken: list[list[int]]
    preference: dict[int, list[int]] = dict()

    def __init__(self):
        self.size = int(sys.stdin.readline())

        for _ in range(self.size ** 2):
            num, f1, f2, f3, f4 = map(int, sys.stdin.readline().split())
            self.preference[num] = [f1, f2, f3, f4]
        
        self.taken = [
            [-1 for _ in range(self.size)] for _ in range(self.size)
        ]
        self.empty = [[4 for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 or i == self.size - 1:
                    self.empty[i][j] -= 1
                if j == 0 or j == self.size - 1:
                    self.empty[i][j] -= 1

    def _in_range(self, row: int, col: int):
        return 0 <= row < self.size and 0 <= col < self.size
    
    def _get_adjacents(self, loc: tuple[int, int]) -> list[tuple[int, int]]:
        row, col = loc
        return [
            (row + dy, col + dx) for dy, dx in DIRS 
            if (
                self._in_range(row + dy, col + dx) 
                and self.taken[row + dy][col + dx] < 0
            )
        ]

    def _get_locs_with_most_adjacents(self, src: int) -> list[tuple[int, int]]:
        cnt = dict()
        max_cnt = 0
        for tgt in self.preference[src]:
            if self.seat.get(tgt, None):
                candidates = self._get_adjacents(self.seat[tgt])
                for loc in candidates:
                    cnt[loc] = cnt.get(loc, 0) + 1
                    max_cnt = max(max_cnt, cnt[loc])
        return [loc for loc in cnt.keys() if cnt[loc] == max_cnt]

    def _get_locs_with_most_empty(
        self, tgts: list[tuple[int, int]]
    ) -> list[tuple[int, int]]:
        if len(tgts) == 0:
            tgts = [(i, j) for i in range(self.size) for j in range(self.size)]
        locs = []
        max_empty = 0
        
        for row, col in tgts:
            if self.empty[row][col] > max_empty:
                max_empty = self.empty[row][col]
                locs = [(row, col)]
            elif self.empty[row][col] == max_empty:
                locs.append((row, col))
        
        return locs

    def _take_seat(self, src: int, row: int, col: int):
        self.seat[src] = (row, col)
        self.taken[row][col] = src
        self.empty[row][col] = -1
        for dy, dx in DIRS:
            if self._in_range(row + dy, col + dx):
                self.empty[row + dy][col + dx] -= 1

    def choose_seat(self, src: int):
        locs_with_most_adjacents = self._get_locs_with_most_adjacents(src)
        
        if len(locs_with_most_adjacents) == 1:
            row, col = locs_with_most_adjacents[0]
            self._take_seat(src, row, col)
        else:
            locs_with_most_empty = self._get_locs_with_most_empty(
                locs_with_most_adjacents
            )
            if len(locs_with_most_empty) > 1:
                locs_with_most_empty.sort(key=lambda x: (x[0], x[1]))
            row, col = locs_with_most_empty[0]
            self._take_seat(src, row, col)

    def get_satisfaction_score(self):
        sum = 0
        for src, prefs in self.preference.items():
            row, col = self.seat[src]
            pref_cnt = 0
            for dy, dx in DIRS:
                if (
                    self._in_range(row + dy, col + dx) 
                    and self.taken[row + dy][col + dx] in prefs
                ):
                    pref_cnt += 1
            sum += int(10 ** (pref_cnt - 1))
        return sum
    
            
def main():
    grid = Grid()
    for src in grid.preference.keys():
        grid.choose_seat(src)
    print(grid.get_satisfaction_score())


if __name__ == "__main__":
    main()
