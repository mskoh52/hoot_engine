from dataclasses import dataclass
from typing import Sequence

import pygame

from .drawable import Drawable


@dataclass(frozen=True)
class CanvasParams:
    width: int
    height: int
    title: str


class Canvas:
    params: CanvasParams
    _screen: pygame.Surface
    _background: pygame.Surface

    def __init__(self, params: CanvasParams):
        self.params = params
        self._screen = pygame.display.set_mode((params.width, params.height))
        self._background = pygame.Surface(self._screen.get_size())
        pygame.display.set_caption(params.title)
        self._drawables = []

    def init_background(self, color: pygame.Color, drawables: Sequence[Drawable]):
        self._background.fill(color)
        for drawable in drawables:
            drawable.draw(self._background)

    def flip(self):
        self._screen.blit(self._background, (0, 0))

        for d in sorted(self._drawables, key=lambda d: d.z):
            if d.visible:
                d.draw(self._screen)

        pygame.display.flip()
