from ..position import Position
from .drawable import Drawable
from .time import TimeInterval


class Animation:
    def __init__(self, drawable: Drawable):
        self._drawable = drawable

    def step(self, t: int):
        pass


class Linear(Animation):
    def __init__(self, drawable: Drawable, start: Position, end: Position, duration: TimeInterval):
        super().__init__(drawable)

        self.start = start
        self.end = end
        self.duration = duration

        self._length = self.end - self.start

        self.velocity = self._length / duration.ticks

    def step(self, t: int):
        self._update_pos(t)

    def _update_pos(self, t: int):
        x0 = self.start
        v = self.velocity

        if t > self.duration.ticks:
            pos = self.end
        else:
            pos = x0 + v * t

        self._drawable.pos = pos
        return self._drawable.pos
