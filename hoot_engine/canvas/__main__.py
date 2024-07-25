import random
import time

import pygame

from ..events import EventHandler, get_events, handle
from ..position import Position
from .animation import Linear
from .canvas import Canvas, CanvasParams
from .drawable import Circle, Rectangle, Sprite, Text, translate
from .time import Time

pygame.init()

time = Time(ticks_per_second=60)

owl = Sprite("./res/owl.png", 64, 64, Position(100, 100), xf=translate(-32, -32))
small_owls = [
    Sprite("./res/owl.png", 32, 32, Position(300, 300), xf=translate(-16, -48)),
    Sprite("./res/owl.png", 32, 32, Position(300, 300), xf=translate(16, 16)),
    Sprite("./res/owl.png", 32, 32, Position(300, 300), xf=translate(-48, 16)),
]
rect = Rectangle(pygame.Color(255, 255, 0), 25, 25, Position(50, 350), z=1)
circle = Circle(pygame.Color(0, 255, 0), 12, Position(50, 350))

rect2 = Rectangle(pygame.Color(255, 255, 0), 25, 25, Position(350, 50))
circle2 = Circle(pygame.Color(0, 255, 0), 12, Position(350, 50), z=1)

anims = [
    Linear(drawable=owl, start=owl.pos, end=Position(300, 300), duration=time.interval(2)),
    Linear(
        drawable=(o := small_owls[0]),
        start=o.pos,
        end=Position(100, 300),
        duration=time.interval(1),
    ),
    Linear(
        drawable=(o := small_owls[1]),
        start=o.pos,
        end=Position(100, 300),
        duration=time.interval(1.2),
    ),
    Linear(
        drawable=(o := small_owls[2]),
        start=o.pos,
        end=Position(100, 300),
        duration=time.interval(0.8),
    ),
    Linear(
        drawable=rect,
        start=rect.pos,
        end=Position(350, 350),
        duration=time.interval(2),
    ),
    Linear(
        drawable=circle,
        start=circle.pos,
        end=Position(350, 350),
        duration=time.interval(2),
    ),
    Linear(
        drawable=rect2,
        start=rect2.pos,
        end=Position(50, 50),
        duration=time.interval(2),
    ),
    Linear(
        drawable=circle2,
        start=circle2.pos,
        end=Position(50, 50),
        duration=time.interval(2),
    ),
]


def _random_color():
    return pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


font = pygame.font.SysFont("Iosevka", 16)
txt = Text(font, pygame.Color((100, 200, 100)), Position(5, 5))

canvas = Canvas(params=CanvasParams(400, 400, "hoot engine"))
canvas._drawables.extend(small_owls)
canvas._drawables.extend([owl, rect, circle, rect2, circle2, txt])

bg_spots = [
    Circle(_random_color(), 5, Position(random.randint(0, 400), random.randint(0, 400)))
    for _ in range(100)
]
canvas.init_background(pygame.Color(0, 0, 0), bg_spots)


class DemoEventHandler(EventHandler):
    @handle([{"type": "QUIT"}, {"type": "KEY", "key": "q"}])
    def handle_quit(self, state):
        return state | {"running": False}

    @handle({"type": "KEY", "key": "space"})
    def handle_trigger_animation(self, state):
        return state | {"animate": True}


event_handler = DemoEventHandler()

state = {"running": True, "animate": False}

t = 0
while state["running"]:
    events = get_events()
    state = event_handler(events, state)

    if not state["running"]:
        break

    if state["animate"]:
        for anim in anims:
            anim.step(t)

        t += 1
        if all(t > anim.duration.ticks for anim in anims):
            state["animate"] = False
            t = 0

    txt.text = f"{t=:03d}, {state=}"

    time.wait_for_tick()

    canvas.flip()


pygame.quit()
