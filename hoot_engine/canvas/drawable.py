import pygame
import numpy as np
from pathlib import Path
from functools import cache

from ..position import Position


@cache
def load_sprite(path: Path | str, w, h):
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, (w, h))
    return image


def translate(x, y):
    return np.array(
        [
            [1, 0, 0],
            [0, 1, 0],
            [x, y, 1],
        ]
    )


class Drawable:
    pos: Position
    visible: bool
    z: int = 0

    def __init__(self, pos: Position, z: int = 0):
        self.pos = pos
        self.visible = True
        self.z = z

    def draw(self, screen: pygame.Surface):
        pass


class Sprite(Drawable):
    w: int
    h: int
    xf: np.ndarray

    def __init__(
        self,
        path: Path | str,
        w: int,
        h: int,
        pos: Position,
        z: int = 0,
        xf: np.ndarray = np.eye(3),
    ):
        super().__init__(pos=pos, z=z)
        self.w = w
        self.h = h
        self.xf = xf
        self._image = load_sprite(path, w, h)

    def draw(self, screen: pygame.Surface):
        screen.blit(self._image, (self.pos @ self.xf).round())


class Text(Drawable):
    def __init__(self, font, color: pygame.Color, pos: Position, z: int = 0):
        super().__init__(pos=pos, z=z)
        self.font = font
        self.text = ""
        self.color = color

    def draw(self, screen: pygame.Surface):
        ts = self.font.render(self.text, False, self.color)
        screen.blit(ts, self.pos.round())


class Circle(Drawable):
    def __init__(self, color: pygame.Color, radius: int, pos: Position, z: int = 0):
        super().__init__(pos=pos, z=z)
        self.color = color
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos.round(), self.radius)


class Rectangle(Drawable):
    def __init__(self, color: pygame.Color, width: int, height: int, pos: Position, z: int = 0):
        super().__init__(pos=pos, z=z)
        self.pos = pos
        self.color = color
        self.width = width
        self.height = height

    def draw(self, screen):
        x, y = self.pos.round()
        pygame.draw.rect(screen, self.color, pygame.Rect(x, y, self.width, self.height))
