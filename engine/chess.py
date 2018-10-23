from util import *
from pieces import *


class Engine(object):

    def __init__(self, fen="default fen"):
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
            for move in board.get_legal_moves()
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
        # self.piece_position = [0 for _ in range(64)]
        # self.

    def get_heuristic_value(self):
        pass

    def set_position(self, position):
        print(position)
        self.position = [0] * 64
        for row_index, row in enumerate(position.split("/")):
            empty_squares = 0
            for column_index, char in enumerate(row):
                if char.isdigit():
                    empty_squares += int(char)
                    continue
                id = Piece.get_id_for_char(char)
                index = column_index + 8 * row_index + empty_squares
                self.position[index] = id

    def set_FEN(self, fen):
        # position, player
        # _color, castling_rights, en_passant = fen.split(" ")
        data = fen.split(" ")
        self.set_position(data[0])
        # self.castling_rights = {
        #     Color.WHITE: [],
        #     Color.BLACK:
        # }
        self.print()

        # self.player_color = player_color

    def print(self):
        out = list(map(lambda x: Piece.get_char_for_id(x), self.position))
        for i in range(8):
            print(out[i * 8:(i + 1) * 8])

    def get_legal_moves(self):

        for piece in self.all_pieces:
            if piece.color == self.player:
                pass

    def make_move(self):
        """perform a move on the board, ONLY CALLED BY MOVE CLASS"""


class BaseMove(object):

    def execute(self, board):
        pass

    def get_description(self):
        return "Base Move"


if __name__ == '__main__':
    board = Board()
    board.set_FEN(DEFAULT_FEN)
    print("-----")
    board.set_FEN("8/8/8/2k5/4K3/8/8/8")
