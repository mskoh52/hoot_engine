import numpy as np
import pytest
from hoot_engine.position import Position


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (Position(5, 6), Position(1, 1), Position(6, 7)),
        (Position(5, 6), np.array([1, 1]), Position(6, 7)),
    ],
)
def test_add(x, y, expected):
    assert x + y == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (Position(5, 6), Position(1, 1), Position(4, 5)),
        (Position(5, 6), np.array([1, 1]), Position(4, 5)),
    ],
)
def test_subtract(x, y, expected):
    assert x - y == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (Position(5, 6), 2, Position(10, 12)),
        (Position(5, 6), -3, Position(-15, -18)),
        (Position(5, 6), 0.5, Position(2.5, 3)),
    ],
)
def test_mul(x, y, expected):
    assert x * y == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (Position(5, 6), 2, Position(2.5, 3)),
        (Position(5, 6), -2, Position(-2.5, -3)),
        (Position(5, 6), 0.5, Position(10, 12)),
    ],
)
def test_div(x, y, expected):
    assert x / y == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (Position(5, 6), np.eye(3), Position(5, 6)),
        (Position(5, 6), 2 * np.eye(3), Position(10, 12)),
        (Position(5, 6), np.array([[1, 3, 0], [-2, 4, 0], [0, 0, 1]]), Position(-7, 39)),
        (Position(5, 6), np.array([[1, 0, 0], [0, 1, 0], [3, 4, 1]]), Position(8, 10)),
    ],
)
def test_matmul(x, y, expected):
    assert x @ y == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        (Position(3.5, 3.4), (4, 3)),
        (Position(3.5, 3.6), (4, 4)),
        (Position(-3.5, -3.4), (-4, -3)),
        (Position(-3.5, -3.6), (-4, -4)),
    ],
)
def test_round(x, expected):
    assert x.round() == expected
