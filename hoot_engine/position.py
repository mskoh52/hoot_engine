from typing import NamedTuple

import numpy as np


class Position(NamedTuple):
    x: float
    y: float

    def round(self) -> tuple[int, int]:
        return (round(self.x), round(self.y))

    def __add__(self, other):
        if isinstance(other, np.ndarray):
            return Position(self.x + other[0], self.y + other[1])

        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, np.ndarray):
            return Position(self.x - other[0], self.y - other[1])

        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Position(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Position(self.x / other, self.y / other)

    def __matmul__(self, other):
        assert isinstance(other, np.ndarray)
        assert other.shape == (3, 3)
        s = (self.x, self.y, 1)
        x, y, *_ = s @ other
        return Position(x.item(), y.item())
