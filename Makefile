all: test hoot

test:
	poetry run pytest

hoot:
	poetry run python -m hoot_engine.canvas
