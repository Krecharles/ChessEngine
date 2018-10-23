class Piece(object):
    """
    Base Piece
    """
    ALL_PIECE_CLASSES = []

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

    def get_legal_moves(self):
        """ Returns a list of every legal move that can be made by moving this piece """
        pass


class Pawn(Piece):
    char = "p"
    ID_WHITE = 1
    ID_BLACK = 7


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
