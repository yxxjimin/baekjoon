import sys


class Grid:
    size: int
    loc_to_ord: dict[int, int]
    marbles: list[int]
    
    def __init__(self, size: int):
        self.size = size
        self.loc_to_ord = self._initialize_loc_to_ord()
        self.marbles = self._initialize_marbles()

    def _initialize_loc_to_ord(self) -> dict[int, int]:
        mid = (self.size + 1) // 2
        row, col = mid, mid
        
        loc_to_ord = {row * self.size + col: 0}
        cnt = 1

        for dist in range(1, mid):
            row -= 1
            col -= 1

            for i in range(8 * dist):
                if i < 2 * dist:
                    row += 1
                elif i < 4 * dist:
                    col += 1
                elif i < 6 * dist:
                    row -= 1
                else:
                    col -= 1
                loc_to_ord[row * self.size + col] = cnt
                cnt += 1

        return loc_to_ord
    
    def _initialize_marbles(self) -> list[int]:
        marbles = [-1 for _ in range(self.size ** 2)]
        for i in range(1, self.size + 1):
            row = list(map(int, sys.stdin.readline().split()))
            for j in range(1, self.size + 1):
                marbles[self.loc_to_ord[i * self.size + j]] = row[j - 1]
        return marbles
        
    def destroy(self, dir: int, dist: int) -> int:
        mid = (self.size + 1) // 2
        directions = {
            1: (-1, 0),
            2: (1, 0),
            3: (0, -1),
            4: (0, 1),
        }
        unit_r, unit_c = directions[dir]

        tgt_ords = [
            self.loc_to_ord[(mid + unit_r * d) * self.size + mid + unit_c * d] 
            for d in range(1, dist + 1)
        ]

        for ord in tgt_ords:
            self.marbles[ord] = -1

        explode_cnt = {1: 0, 2: 0, 3: 0}
        exploded, cnts = self._explode()

        while exploded:
            for k in explode_cnt:
                explode_cnt[k] += cnts[k]
            self._clean()
            exploded, cnts = self._explode()

        self._regroup()

        return sum([k * explode_cnt[k] for k in explode_cnt])

    def _explode(self) -> tuple[bool, dict[int, int]]:
        exploded = False
        explode_cnt = {1: 0, 2: 0, 3: 0}

        for num, start, end, cnt in self._find_groups():
            if cnt >= 4:
                self.marbles[start:end] = [-1 for _ in range(end - start)]
                explode_cnt[num] += cnt
                exploded = True

        return exploded, explode_cnt

    def _resize(self):
        total_len = self.size ** 2
        if len(self.marbles) < total_len:
            self.marbles += [0 for _ in range(total_len - len(self.marbles))]
        else:
            self.marbles = self.marbles[:total_len]
    
    def _clean(self):
        self.marbles = [x for x in self.marbles if x != -1]

    def _find_groups(self) -> list[tuple[int, int, int, int]]:
        groups = []
        start = 1
        streak = 0

        for i in range(1, len(self.marbles)):
            if self.marbles[i] == self.marbles[start]:
                streak += 1
            elif self.marbles[i] != -1:
                if self.marbles[start] > 0:
                    groups.append((self.marbles[start], start, i, streak))
                streak = 1
                start = i

        if self.marbles[-1] != 0:
            groups.append(
                (self.marbles[start], start, len(self.marbles), streak)
            )

        return groups
    
    def _regroup(self):
        new_marbles = [0]

        for num, _, _, cnt in self._find_groups():
            new_marbles += [cnt, num]
        
        self.marbles = new_marbles
        self._resize()


def main():
    n, m = map(int, sys.stdin.readline().split())
    answer = 0
    grid = Grid(n)

    for _ in range(m):
        dir, dist = map(int, sys.stdin.readline().split())
        answer += grid.destroy(dir, dist)

    print(answer)


if __name__ == "__main__":
    main()
