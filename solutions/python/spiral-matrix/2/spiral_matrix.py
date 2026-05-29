from typing import Generator, Iterable

DIRECTIONS = ((0, 1), (-1, 0), (1, 0), (0, -1))  # down, left, right, up


class AlreadySetError(Exception):
    pass

def _direction_generator() -> Generator[tuple[int, int]]:
    i = 0
    while True:
        yield DIRECTIONS[i % len(DIRECTIONS)]
        i += 1


def _blank_matrix(size: int) -> list[list[int | None]]:
    return [[None for _ in range(size)] for _ in range(size)]

def _vector_add(v1: Iterable[int], v2: Iterable[int]) -> list[int]:
    return [i + j for i, j in zip(v1, v2)]

def spiral_matrix(size: int, step: int = 1) -> list[list[int]]:
    if size == 0:
        return []

    matrix = _blank_matrix(size)

    matrix[0] = list(range(1, size + 1))

    pos_x, pos_y = size - 1, 0
    numbers = range(size + 1, size ** 2 + 1)
    directions = _direction_generator()
    current_direction = next(directions)

    for num in numbers:
        while True:
            try:
                next_pos_x, next_pos_y = _vector_add((pos_x, pos_y), current_direction)
                if matrix[next_pos_y][next_pos_x] is not None:
                    raise AlreadySetError
                matrix[next_pos_y][next_pos_x] = num

                pos_x, pos_y = next_pos_x, next_pos_y
            except (IndexError, AlreadySetError): # I'm glad Python 3.14 exists, so I don't need parentheses here
                current_direction = next(directions)
            else:
                break

    if not all([all(row) for row in matrix]):
        raise RuntimeError('Not all numbers were set in the matrix, something went wrong')

    return matrix

if __name__ == '__main__':
    print(spiral_matrix(4))
