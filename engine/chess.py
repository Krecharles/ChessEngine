from util import *
from pieces import *
import copy


class Engine(object):

    def __init__(self):
        self.board = Board()

    def setFEN(self, fen):
        self.player = Color.WHITE
        self.board.set_FEN(fen)

    def get_best_move(self, move_depth=1):
        score, move = self.min_max(self.board, move_depth, self.player)
        return move

    def min_max(self, board, depth, maximizing_player):
        if depth == 0:  # or board.is_mated():
            return board.get_heuristic_value(), None
        best_move = None
        if maximizing_player == Color.WHITE:
            value = -(2 ** 32)
            for move in board.get_legal_moves():
                new_board = board.make_legal_move(move)
                new_value, _ = self.min_max(new_board, depth - 1, Color.BLACK)
                if new_value > value:
                    value = new_value
                    best_move = move
        else:
            value = 2 ** 32
            for move in board.get_legal_moves():
                new_board = board.make_legal_move(move)
                new_value, _ = self.min_max(new_board, depth - 1, Color.WHITE)
                if new_value < value:
                    value = new_value
                    best_move = move

        return value, best_move


class Board:

    def get_heuristic_value(self):
        # returns the sum of all the positive and negative heuristic values,
        # is positive if white is winning and negative if black is winning
        out = 0
        for id in self.position:
            if id == Piece.ID_PIECE_NONE:
                continue
            val = Piece.get_piece_class_of_id(id).HEURISTIC_VALUE
            is_white = id < 7
            out += val if is_white else -val
        return out

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

    def __str__(self):
        positions = list(map(lambda x: Piece.get_char_for_id(x), self.position))
        out = ""
        for i in range(8)[::-1]:
            out += (str(i + 1) + "| " + str(
                positions[i * 8:(i + 1) * 8]).replace("'", "")
                    .replace(",", "").replace("[", "").replace("]", ""))
            out += "\n"
        out += "   ---------------\n"
        out += "   a b c d e f g h"
        return out

    def print(self):
        print("------------------------------")
        print(str(self))
        print("------------------------------")

    def get_legal_moves(self):
        all_moves = []
        for pos, id in enumerate(self.position):
            if id == Piece.ID_PIECE_NONE:
                continue
            # it does not matter which if statement is used performance wise
            # if (id < 7) == (self.player_color == Color.WHITE):
            if self.get_color_at(pos) == self.player_color:
                piece = Piece.get_piece_class_of_id(id)
                all_moves.extend(piece.get_legal_moves(self, pos))
        return all_moves

    def is_empty(self, tile):
        return self.position[tile] == Piece.ID_PIECE_NONE

    def get_color_at(self, tile):
        if self.position[tile] == Piece.ID_PIECE_NONE:
            return Color.NONE
        if self.position[tile] < 7:
            return Color.WHITE
        return Color.BLACK

    def make_legal_move(self, move):
        """assumes the given move is legal"""
        new_board = self.copy()
        piece = Piece.get_piece_class_of_id(self.position[move.tile_from])
        piece.swap(new_board, move)
        return new_board

    def make_move(self, move):
        """perform a move on the board, non mutable so returns new board"""
        if self.is_empty(move.tile_from):
            print("illegal move")
            return self
        new_board = copy.deepcopy(self)
        piece = Piece.get_piece_class_of_id(self.position[move.tile_from])
        piece.move(new_board, move)
        return new_board

    def copy(self):
        b = Board()
        b.position = [x for x in self.position]
        # b.castling_rights = copy.deepcopy(self.castling_rights)
        b.en_passant = self.en_passant
        b.player_color = self.player_color
        return b


def move(_board, move_str):
    move = Move.from_notation(move_str)
    new_board = _board.make_move(move)
    return new_board


def play_alone():
    board = Board()
    board.set_FEN(DEFAULT_FEN)

    all_boards = [board]
    while True:
        cmd = input("Your next Move: ")
        if cmd == "undo":
            all_boards.pop()
            board = all_boards[-1]
            continue
        if cmd == "print":
            board.print()
            continue
        move = Move.from_notation(cmd)
        new_board = board.make_move(move)
        board = new_board
        all_boards.append(board)


if __name__ == '__main__':
    engine = Engine()
    engine.setFEN(DEFAULT_FEN)
    print(engine.get_best_move(3))
    print(calls)
