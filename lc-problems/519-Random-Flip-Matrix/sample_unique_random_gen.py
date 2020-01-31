#!/usr/bin/env python


class Solution:
    def __init__(self, n_rows: int, n_cols: int):
        self.rows, self.cols = n_rows, n_cols
        self.index = None
        self.reset()

    def flip(self) -> List[int]:
        i = next(self.index)
        return [i//self.cols, i % self.cols]

    def reset(self) -> None:
        self.index = self.sample(self.cols*self.rows)

    def ceiling_pow2(self, n: int) -> int:
        return 2**(n-1).bit_length() if n else 1

    def sample(self, count: int) -> int:
        modulo = self.ceiling_pow2(count)
        result = random.randint(0, count)

        for _ in range(count):
            while True:
                result = (result * 5 + 1) % modulo
                if result < count:
                    break
            yield result
