from util import *
from pieces import *
import copy


class Engine(object):

    def __init__(self):
        self.board = Board()

    def setFEN(self, fen):
        self.player = Color.WHITE
        pass

    def get_best_move(self, move_depth=1):
        #  for move in possible_moves
        d = self.min_max(self.board, move_depth, self.player)
        return d

    def min_max(self, board, depth, maximizing_player):
        if depth == 0 or board.is_mated():
            return board.get_heuristic_value()
        if maximizing_player == Color.WHITE:
            value = -(2 ** 32)
            for move in board.get_legal_moves():
                new_board = move.execute(board)
                new_value = self.min_max(new_board, depth - 1, Color.BLACK)
                value = max(value, new_value)
        else:
            value = 2 ** 32
            for move in board.get_legal_moves():
                new_board = move.execute(board)
                new_value = self.min_max(new_board, depth - 1, Color.WHITE)
                value = min(value, new_value)
        return value


class Board(object):

    def __init__(self):
        self.move_history = []

    def get_heuristic_value(self):
        pass

    def set_position(self, position):
        self.position = [Piece.ID_PIECE_NONE] * 64
        for row_index, row in enumerate(position.split("/")[::-1]):
            empty_squares = 0
            for column_index, char in enumerate(row):
                if char.isdigit():
                    empty_squares += int(char) - 1
                    continue
                id = Piece.get_id_for_char(char)
                index = column_index + 8 * row_index + empty_squares
                self.position[index] = id

    def set_FEN(self, fen):
        data = fen.split(" ")

        self.set_position(data[0])

        self.player_color = Color.WHITE if data[1] == "w" else Color.BLACK

        self.castling_rights = {
            Color.WHITE: [King.char.capitalize() in data[2],
                          Queen.char.capitalize() in data[2]],
            Color.BLACK: [King.char in data[2], Queen.char in data[2]]
        }

        # -1 means no en_passant possible, else the id of the tile is returned
        self.en_passant = data[3] if data[3] != "-" else -1
        self.print()

    def __str__(self):
        positions = list(map(lambda x: Piece.get_char_for_id(x), self.position))
        out = ""
        for i in range(8)[::-1]:
            out += (str(positions[i * 8:(i + 1) * 8]).replace("'", "")
                  .replace(",", "").replace("[", "").replace("]", ""))
            out += "\n" if i is not 0 else ""
        return out

    def print(self):
        print("---------------")
        print(str(self))
        print("---------------")

    def get_legal_moves(self):
        for piece in self.all_pieces:
            if piece.color == self.player:
                pass

    def is_empty(self, tile):
        return self.position[tile] == Piece.ID_PIECE_NONE

    def make_move(self, move):
        """perform a move on the board, non mutable so returns new board"""
        if self.is_empty(move.tile_from):
            return print("illegal move")
        new_board = copy.deepcopy(self)
        piece = Piece.get_piece_class_of_id(self.position[move.tile_from])
        piece.move(new_board, move)
        self.print() # for debugging purposes
        return new_board


class BaseMove(object):

    def execute(self, board):
        pass

    def get_description(self):
        return "Base Move"


if __name__ == '__main__':
    board = Board()
    board.set_FEN(DEFAULT_FEN)
    move = Move.from_notation("a2a3")
    new_board = board.make_move(move)
