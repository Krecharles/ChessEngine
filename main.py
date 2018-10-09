import server_communication as sc
from engine import stockfish
import time
import sys


def make_move():
    position = sc.get_game_position()
    print(position)
    stockfish.set_fen_position(position)
    best_move = stockfish.get_best_move()
    print(best_move)
    sc.make_move(best_move)


def can_move():
    return sc.get_game_json() is not None


if __name__ == '__main__':

    sc.game_id = sys.argv[1]
    sc.is_black = 0 if sys.argv[2] == "white" else 1
    print("starting game with id {}".format(sc.game_id))

    last_activity = "0"
    while True:
        print("looping")
        new_activity = sc.get_last_activity()
        if last_activity == new_activity:
            time.sleep(5)
            continue
        print("the game was updated")
        last_activity = new_activity

        if can_move():
            make_move()
            time.sleep(10)
