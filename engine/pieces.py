from util import *


class Piece(object):
    """
    Base Piece
    """
    ALL_PIECE_CLASSES = []
    ID_PIECE_NONE = 0

    @staticmethod
    def get_id_for_char(char):
        for piece in Piece.ALL_PIECE_CLASSES:
            if piece.char == char.lower():
                if piece.char == char:
                    return piece.ID_WHITE
                return piece.ID_BLACK

    @staticmethod
    def get_char_for_id(id):
        for piece in Piece.ALL_PIECE_CLASSES:
            if piece.ID_WHITE == id:
                return piece.char
            if piece.ID_BLACK == id:
                return piece.char.upper()
        return id

    @staticmethod
    def get_piece_class_of_char(char):
        return list(filter(lambda klass: klass.char == char.lower(),
                           Piece.ALL_PIECE_CLASSES))[0]

    @staticmethod
    def get_piece_class_of_id(id):
        """id != 0"""
        return list(
            filter(lambda klass: klass.ID_WHITE == id or klass.ID_BLACK == id,
                   Piece.ALL_PIECE_CLASSES))[0]

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


class Move:

    def __init__(self, tile_from, tile_to):
        self.tile_from = tile_from
        self.tile_to = tile_to

    @classmethod
    def from_notation(cls, notation):
        return cls(convert_tile_to_id(notation[:2]),
                   convert_tile_to_id(notation[2:]))


class Pawn(Piece):
    char = "p"
    ID_WHITE = 1
    ID_BLACK = 7

    @staticmethod
    def get_legal_moves(board, position):
        destinations = []

        if board.player_color == Color.WHITE:
            # normal advance pawn move
            if position + 8 <= 63:
                if board.is_empty(position + 8):
                    destinations.append(position + 8)

            # jump 2 rows move
            if position in range(8, 15):
                if board.is_empty(position + 8) and board.is_empty(position + 16):
                    destinations.append(position + 16)

            # take left
            if position % 8 != 0:
                if not board.is_empty(position + 7):

        return list(map(lambda x: Move(position, x), destinations))

    @staticmethod
    def move(board, move):
        if move in Pawn.get_legal_moves(board, move.tile_from):
            return print("Illegal Move")

        Piece.swap(board, move)


class Rook(Piece):
    char = "r"
    ID_WHITE = 2
    ID_BLACK = 8


class Knight(Piece):
    char = "n"
    ID_WHITE = 3
    ID_BLACK = 9


class Bishop(Piece):
    char = "b"
    ID_WHITE = 4
    ID_BLACK = 10


class Queen(Piece):
    char = "q"
    ID_WHITE = 5
    ID_BLACK = 11


class King(Piece):
    char = "k"
    ID_WHITE = 6
    ID_BLACK = 12


Piece.ALL_PIECE_CLASSES = [Pawn, Rook, Knight, Bishop, Queen, King]
