from engine.chess import *


def test_create_board_from_fen():
    b = Board()
    b.set_FEN(
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    assert b.position == [8, 9, 10, 11, 12, 10, 9, 8, 7, 7, 7, 7, 7, 7, 7, 7, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
                          1, 1, 1, 2, 3, 4, 5, 6, 4, 3, 2]

    b.set_FEN("rnbqkbnr/ppppppPp/8/8/4P3/PP6/2PP1P1P/RNBQKBNR b KQkq - 0 1")
    assert b.position == [8, 9, 10, 11, 12, 10, 9, 8, 0, 0, 7, 7, 0, 7, 0, 7, 7,
                          7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
                          1, 7, 1, 2, 3, 4, 5, 6, 4, 3, 2]
    b.set_FEN(
        "2b1k1nr/ppp1np1p/4p3/b1N3P1/1P1qP1Q1/P2R4/2N2P1P/RKB2r2 b - - 0 1")
    assert b.position == [8, 12, 10, 0, 0, 2, 0, 0, 0, 0, 9, 0, 0, 7, 0, 7, 7,
                          0, 0, 8, 0, 0, 0, 0, 0, 7, 0, 5, 7, 0, 11, 0, 4, 0, 9,
                          0, 0, 0, 7, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 3,
                          1, 0, 1, 0, 0, 4, 0, 6, 0, 3, 2]
