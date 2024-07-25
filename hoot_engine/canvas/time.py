import pygame


class TimeInterval:
    def __init__(self, secs: int, ticks_per_second: int):
        self.secs = secs
        self.ticks_per_second = ticks_per_second

    @property
    def ticks(self):
        return self.secs * self.ticks_per_second


class Time:
    def __init__(self, ticks_per_second: int):
        self.ticks_per_second = ticks_per_second
        self._clock = pygame.time.Clock()

    def wait_for_tick(self):
        self._clock.tick(self.ticks_per_second)

    def interval(self, secs):
        return TimeInterval(secs, self.ticks_per_second)
