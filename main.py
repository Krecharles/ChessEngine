import server_communication as sc
from engine import stockfish
import time
import datetime


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def make_move(game):
    position = game["fen"]
    stockfish.set_fen_position(
        position if position is not None else "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    best_move = stockfish.get_best_move()
    sc.make_move(game, best_move)


if __name__ == '__main__':

    while True:
        print(bcolors.OKGREEN + "[LOOPING]: {}".format(datetime.datetime.now()) + bcolors.ENDC)
        for game in sc.get_all_games():
            if game["isMyTurnToMove"]:
                make_move(game)
                continue
        # sc.create_game()
        time.sleep(10)
