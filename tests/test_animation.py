from hoot_engine.canvas.animation import Linear
from hoot_engine.canvas.drawable import Drawable
from hoot_engine.canvas.position import Position
from hoot_engine.canvas.time import TimeInterval


def test_linear():
    drawable = Drawable(Position(0, 0))
    anim = Linear(
        drawable=drawable, start=drawable.pos, end=Position(10, 20), duration=TimeInterval(10, 1)
    )

    for t in range(15):
        anim.step(t)
        if t >= anim.duration.ticks:
            assert drawable.pos == anim.end, f"{t=}, {drawable.pos=}"
        else:
            assert drawable.pos == Position(t, 2 * t), f"{t=}, {drawable.pos=}"


def test_linear_negative():
    drawable = Drawable(Position(0, 0))
    anim = Linear(
        drawable=drawable, start=drawable.pos, end=Position(10, -20), duration=TimeInterval(10, 1)
    )

    for t in range(15):
        anim.step(t)
        if t >= anim.duration.ticks:
            assert drawable.pos == anim.end, f"{t=}, {drawable.pos=}"
        else:
            assert drawable.pos == Position(t, -2 * t), f"{t=}, {drawable.pos=}"


def test_linear_not_divisible():
    drawable = Drawable(Position(0, 0))
    anim = Linear(
        drawable=drawable, start=drawable.pos, end=Position(10, -20), duration=TimeInterval(11, 1)
    )

    for t in range(15):
        anim.step(t)
        if t >= anim.duration.ticks:
            assert drawable.pos == anim.end, f"{t=}, {drawable.pos=}"
        else:
            assert drawable.pos == Position(10 / 11 * t, -20 / 11 * t), f"{t=}, {drawable.pos=}"
