from util import *


class Piece(object):
    """
    Base Piece
    """
    ALL_PIECE_CLASSES = []
    ID_PIECE_NONE = 0
    HEURISTIC_VALUE = 0

    @staticmethod
    def get_id_for_char(char):
        for piece in Piece.ALL_PIECE_CLASSES:
            if piece.char == char.lower():
                if char.isupper():
                    return piece.ID_WHITE
                return piece.ID_BLACK

    @staticmethod
    def get_char_for_id(id):
        for piece in Piece.ALL_PIECE_CLASSES:
            if piece.ID_WHITE == id:
                return piece.char.upper()
            if piece.ID_BLACK == id:
                return piece.char.lower()

        return id

    @staticmethod
    def get_piece_class_of_char(char):
        return list(filter(lambda klass: klass.char == char.lower(),
                           Piece.ALL_PIECE_CLASSES))[0]

    @staticmethod
    def get_piece_class_of_id(id):
        return Piece.OPTIMIZED_PIECE_CLASSES[id]
        # if id == 0:
        #     return Piece
        # return list(
        #     filter(lambda klass: klass.ID_WHITE == id or klass.ID_BLACK == id,
        #            Piece.ALL_PIECE_CLASSES))[0]

    @staticmethod
    def get_legal_moves(board, position):
        """
        Returns a list of every legal move that can be made by moving this piece
        """
        pass

    @staticmethod
    def swap(self, move):
        self.position[move.tile_to] = self.position[move.tile_from]
        self.position[move.tile_from] = Piece.ID_PIECE_NONE

    @staticmethod
    def move(board, move):
        piece = Piece.get_piece_class_of_id(board.position[move.tile_from])
        legal_moves = piece.get_legal_moves(board, move.tile_from)
        if move not in legal_moves:
            print("Illegal Move")
            return

        Piece.swap(board, move)

class Move:

    def __init__(self, tile_from, tile_to):
        self.tile_from = tile_from
        self.tile_to = tile_to

    def __eq__(self, o: object) -> bool:
        return o.tile_from == self.tile_from and o.tile_to == self.tile_to

    @classmethod
    def from_notation(cls, notation):
        return cls(convert_tile_to_id(notation[:2]),
                   convert_tile_to_id(notation[2:]))

    def __str__(self):
        return "{} -> {}".format(self.tile_from, self.tile_to)


class Pawn(Piece):
    char = "p"
    ID_WHITE = 1
    ID_BLACK = 7
    HEURISTIC_VALUE = 1

    @staticmethod
    def get_legal_moves(board, position):
        destinations = []

        if board.get_color_at(position) == Color.WHITE:
            # normal advance pawn move
            if position + 8 <= 63:
                if board.is_empty(position + 8):
                    destinations.append(position + 8)

            # jump 2 rows move
            if position in range(8, 16):
                if board.is_empty(position + 8) and board.is_empty(
                        position + 16):
                    destinations.append(position + 16)

            # take left
            if position % 8 != 0 and position + 7 < 64:
                # piece is not on left border and exists
                if board.get_color_at(position + 7) == Color.BLACK:
                    destinations.append(position + 7)

            # take right
            if position % 8 != 7 and position + 9 < 64:
                if board.get_color_at(position + 9) == Color.BLACK:
                    destinations.append(position + 9)

        elif board.get_color_at(position) == Color.BLACK:
            # normal advance pawn move
            if position - 8 >= 0:
                if board.is_empty(position - 8):
                    destinations.append(position - 8)

            # jump 2 rows move
            if position in range(48, 56):
                if board.is_empty(position - 8) and board.is_empty(
                        position - 16):
                    destinations.append(position - 16)

            # take left
            if position % 8 != 0 and position - 9 >= 0:
                # piece is not on left border and exists
                if board.get_color_at(position - 9) == Color.WHITE:
                    destinations.append(position - 9)

            # take right
            if position % 8 != 7 and position - 7 >= 0:
                if board.get_color_at(position - 7) == Color.WHITE:
                    destinations.append(position - 7)

        else:
            print("empty tile")

        return list(map(lambda x: Move(position, x), destinations))


class Rook(Piece):
    char = "r"
    ID_WHITE = 2
    ID_BLACK = 8
    HEURISTIC_VALUE = 5

    @staticmethod
    def get_moves_in_dir(board, position, xDir, yDir):
        destinations = []
        return destinations

    @staticmethod
    def get_legal_moves(board, position):
        destinations = []

        # move left
        for i in range(1, position % 8 + 1):
            pos = position - i
            if board.is_empty(pos):
                destinations.append(pos)
                continue
            elif board.get_color_at(pos) == board.get_color_at(position):
                break
            else:
                destinations.append(pos)
                break

        # move right
        for i in range(1, 8 - (position % 8)):
            pos = position + i
            if board.is_empty(pos):
                destinations.append(pos)
                continue
            elif board.get_color_at(pos) == board.get_color_at(position):
                break
            else:
                destinations.append(pos)
                break

        # move down
        for i in range(1, (position // 8) + 1):
            pos = position - i * 8
            if board.is_empty(pos):
                destinations.append(pos)
                continue
            elif board.get_color_at(pos) == board.get_color_at(position):
                break
            else:
                destinations.append(pos)
                break

        # move up
        for i in range(1, 8 - (position // 8)):
            pos = position + i * 8
            if board.is_empty(pos):
                destinations.append(pos)
                continue
            elif board.get_color_at(pos) == board.get_color_at(position):
                break
            else:
                destinations.append(pos)
                break

        return list(map(lambda x: Move(position, x), destinations))


class Knight(Piece):
    char = "n"
    ID_WHITE = 3
    ID_BLACK = 9
    HEURISTIC_VALUE = 3

    @staticmethod
    def get_legal_moves(board, position):
        destinations = []

        if x(position) >= 2:
            # add left extreme moves
            if y(position) >= 1:
                # add down
                destinations.append(position - 10)
            if y(position) <= 6:
                # add up
                destinations.append(position + 6)
        if x(position) >= 1:
            # add left moves
            if y(position) >= 2:
                # add down
                destinations.append(position - 17)
            if y(position) <= 5:
                # add up
                destinations.append(position + 15)

        if x(position) <= 5:
            # add right extreme moves
            if y(position) >= 1:
                # add down
                destinations.append(position - 6)
            if y(position) <= 6:
                # add up
                destinations.append(position + 10)
        if x(position) <= 6:
            # add right moves
            if y(position) >= 2:
                # add down
                destinations.append(position - 15)
            if y(position) <= 5:
                # add up
                destinations.append(position + 17)

        filtered = filter(
            lambda x: board.get_color_at(x) != board.get_color_at(position),
            destinations)
        return list(map(lambda x: Move(position, x), filtered))


class Bishop(Piece):
    char = "b"
    ID_WHITE = 4
    ID_BLACK = 10
    HEURISTIC_VALUE = 3

    @staticmethod
    def get_legal_moves(board, position):
        destinations = []

        # add left up
        for i in range(1, min(x(position), 8 - y(position))):
            new_pos = i * 7
            if board.is_empty(new_pos):
                destinations.append(new_pos)
                continue
            if board.get_color_at(new_pos) != board.get_color_at(position):
                destinations.append(new_pos)
                break
            if board.get_color_at(new_pos) == board.get_color_at(position):
                break

        # add left down
        for i in range(1, min(x(position), y(position))):
            new_pos = i * -9
            if board.is_empty(new_pos):
                destinations.append(new_pos)
                continue
            if board.get_color_at(new_pos) != board.get_color_at(position):
                destinations.append(new_pos)
                break
            if board.get_color_at(new_pos) == board.get_color_at(position):
                break

        # add right up
        for i in range(1, min(8 - x(position), 8 - y(position))):
            new_pos = i * 9
            if board.is_empty(new_pos):
                destinations.append(new_pos)
                continue
            if board.get_color_at(new_pos) != board.get_color_at(position):
                destinations.append(new_pos)
                break
            if board.get_color_at(new_pos) == board.get_color_at(position):
                break

        # add right down
        for i in range(1, min(8 - x(position), y(position))):
            new_pos = i * -7
            if board.is_empty(new_pos):
                destinations.append(new_pos)
                continue
            if board.get_color_at(new_pos) != board.get_color_at(position):
                destinations.append(new_pos)
                break
            if board.get_color_at(new_pos) == board.get_color_at(position):
                break

        return list(map(lambda x: Move(position, x), destinations))


class Queen(Piece):
    char = "q"
    ID_WHITE = 5
    ID_BLACK = 11
    HEURISTIC_VALUE = 9

    @staticmethod
    def get_legal_moves(board, position):
        return (Rook.get_legal_moves(board, position)
                + Bishop.get_legal_moves(board, position))


class King(Piece):
    char = "k"
    ID_WHITE = 6
    ID_BLACK = 12
    HEURISTIC_VALUE = 2 ** 32 - 1

    @staticmethod
    def get_legal_moves(board, position):
        destinations = []

        touches_left_border = not (x(position) > 0)
        touches_right_border = not (x(position) < 7)
        touches_bottom_border = not (y(position) > 0)
        touches_top_border = not (y(position) < 7)

        if not touches_left_border:
            destinations.append(position - 1)
            if not touches_bottom_border:
                destinations.append(position - 9)
            if not touches_top_border:
                destinations.append(position + 7)

        if not touches_right_border:
            destinations.append(position + 1)
            if not touches_bottom_border:
                destinations.append(position - 7)
            if not touches_top_border:
                destinations.append(position + 9)

        if not touches_top_border:
            destinations.append(position + 8)
        if not touches_bottom_border:
            destinations.append(position - 8)

        filtered = filter(
            lambda x: board.get_color_at(x) != board.get_color_at(position),
            destinations)
        return list(map(lambda x: Move(position, x), filtered))


Piece.ALL_PIECE_CLASSES = [Pawn, Rook, Knight, Bishop, Queen, King]
Piece.OPTIMIZED_PIECE_CLASSES = [Piece, Pawn, Rook, Knight, Bishop, Queen, King,
                                 Pawn, Rook, Knight, Bishop, Queen, King]
