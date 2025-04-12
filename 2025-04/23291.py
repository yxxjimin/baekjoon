import collections
import sys


class FishTankContainer:
    n: int
    tanks: collections.deque[list[int]]

    def __init__(self, n: int):
        self.n = n
        self.tanks = collections.deque(
            map(lambda x: [int(x)], sys.stdin.readline().split())
        )
    
    def _add_fishes(self):
        min_fishes = min([cnt for cnt, in self.tanks])
        for i in range(self.n):
            if self.tanks[i][0] == min_fishes:
                self.tanks[i][0] += 1

    def _stack_first_col(self):
        col = self.tanks.popleft()
        self.tanks[0] += col

    def _is_rotatable(self) -> bool:
        height = len(self.tanks[0])
        for idx, col in enumerate(self.tanks):
            if len(col) == 1:
                return len(self.tanks) - idx >= height
        return False

    def _get_cols_to_rotate(self) -> list[list[int]]:
        stack = []
        while len(self.tanks[0]) > 1:
            col = self.tanks.popleft()
            stack.append(col)
        return stack

    def _rotate_clockwise_and_place(self):
        stack = self._get_cols_to_rotate()
        while len(stack) > 0:
            col = stack.pop()
            height = len(col)
            for i in range(height):
                fishes = col[i]
                self.tanks[i].append(fishes)
                
    def _get_fish_delta(self) -> list[list[int]]:
        delta = [[0 for _ in range(len(col))] for col in self.tanks]
        
        for i in range(len(self.tanks)):
            curr_col = self.tanks[i]
            next_col = self.tanks[i + 1] if i < len(self.tanks) - 1 else []
            for j in range(len(curr_col)):
                if j != len(curr_col) - 1:
                    v_delta = abs(curr_col[j] - curr_col[j + 1]) // 5
                    if v_delta > 0:
                        v_delta = (
                            v_delta 
                            if curr_col[j] < curr_col[j + 1] else -v_delta
                        )
                        delta[i][j] += v_delta
                        delta[i][j + 1] -= v_delta
                if j < len(next_col):
                    h_delta = abs(curr_col[j] - next_col[j]) // 5
                    if h_delta > 0:
                        h_delta = (
                            h_delta if curr_col[j] < next_col[j] else -h_delta
                        )
                        delta[i][j] += h_delta
                        delta[i + 1][j] -= h_delta

        return delta

    def _rearrange_fishes(self):
        delta = self._get_fish_delta()
        for i in range(len(delta)):
            for j in range(len(delta[i])):
                self.tanks[i][j] += delta[i][j]

    def _flatten_tanks(self):
        new_tanks = collections.deque([])
        for col in self.tanks:
            new_tanks += [[fish] for fish in col]
        self.tanks = new_tanks

    def _halve_and_stack_tanks(self):
        stack = []
        for _ in range(len(self.tanks) // 2):
            stack.append(self.tanks.popleft())
        for i in range(len(self.tanks)):
            col = stack.pop()
            self.tanks[i] += reversed(col)

    def step(self) -> int:
        self._add_fishes()
        self._stack_first_col()
        while self._is_rotatable():
            self._rotate_clockwise_and_place()
        self._rearrange_fishes()
        self._flatten_tanks()
        self._halve_and_stack_tanks()
        self._halve_and_stack_tanks()
        self._rearrange_fishes()
        self._flatten_tanks()

        flattened = [fishes for col in self.tanks for fishes in col]
        return max(flattened) - min(flattened)


def main():
    n, k = map(int, sys.stdin.readline().split())
    trials = 0

    grid = FishTankContainer(n)
    while True:
        diff = grid.step()
        trials += 1
        if diff <= k:
            print(trials)
            break


if __name__ == "__main__":
    main()
