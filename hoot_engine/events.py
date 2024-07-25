from typing import Iterable

import pygame

from .position import Position


def get_events() -> list[dict]:
    def dispatch(event: pygame.event.Event) -> dict | None:
        if event.type == pygame.QUIT:
            return {"type": "QUIT"}
        elif event.type == pygame.KEYDOWN:
            return {"type": "KEY", "key": pygame.key.name(event.key)}
        elif event.type == pygame.MOUSEBUTTONUP:
            return {"type": "MOUSE_CLICK", "pos": Position(*event.pos), "button": event.button}

    return list(filter(None, map(dispatch, pygame.event.get())))


def handle(events: dict | Iterable[dict]):
    if isinstance(events, dict):
        events = [events]

    def decorator(f):
        f._events = [tuple(event.items()) for event in events]
        return f

    return decorator


class HandlerMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._registry = {
            event: func
            for func in dct.values()
            if callable(func) and hasattr(func, "_events")
            for event in func._events
        }


class EventHandler(metaclass=HandlerMeta):
    _registry = {}

    def __call__(self, events: Iterable[dict], state):
        for event in events:
            key = tuple(event.items())
            if key not in self._registry:
                continue

            state = self._registry[key](self, state)
        return state
