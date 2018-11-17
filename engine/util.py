DEFAULT_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


class Color:
    WHITE = 0
    BLACK = 1
    NONE = 2


def convert_tile_to_id(tile):
    char, num = tile
    return "abcdefgh".find(char) + (int(num) - 1) * 8


def mapx(arr, mapping):
    return list(map(mapping, arr))


def arr_string(arr):
    return mapx(arr, lambda x: str(x))


def x(position):
    return position % 8


def y(position):
    return position // 8
