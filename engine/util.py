DEFAULT_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


class Color:
    WHITE = 0
    BLACK = 1

def convert_tile_to_id(tile):
    char, num = tile
    return "abcdefgh".find(char) + (int(num)-1) * 8
