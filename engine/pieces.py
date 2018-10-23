from util import *


class Piece(object):
    """
    Base Piece
    """
    ALL_PIECE_CLASSES = []
    ID_PIECE_NONE = 0

    def get_id_for_char(char):
        for piece in Piece.ALL_PIECE_CLASSES:
            if piece.char == char.lower():
                if piece.char == char:
                    return piece.ID_WHITE
                return piece.ID_BLACK

    def get_char_for_id(id):
        for piece in Piece.ALL_PIECE_CLASSES:
            if piece.ID_WHITE == id:
                return piece.char
            if piece.ID_BLACK == id:
                return piece.char.upper()
        return id

    def get_piece_class_of_char(char):
        return list(filter(lambda klass: klass.char == char.lower(), Piece.ALL_PIECE_CLASSES))[0]

    def get_piece_class_of_id(id):
        """id != 0"""
        return list(filter(lambda klass: klass.ID_WHITE == id or klass.ID_BLACK == id, Piece.ALL_PIECE_CLASSES))

    def get_legal_moves(self):
        """ Returns a list of every legal move that can be made by moving this piece """
        pass

    def swap(board, tile_from, tile_to):
        board.position[tile_to] = board.position[tile_from]
        board.position[tile_from] = Piece.ID_PIECE_NONE


class Pawn(Piece):
    char = "p"
    ID_WHITE = 1
    ID_BLACK = 7

    def move(board, tile_from, tile_to):
        # todo check for right color?
        if tile_to == tile_from + 8 and board.is_empty(tile_to):
            # white moves one up
            Piece.swap(board, tile_from, tile_to)
            return

        print("Illegal move")
        # todo raise error
        # todo check other moves by pawn (en_passant etc)


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
