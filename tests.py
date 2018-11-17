from engine.chess import *


def test_create_board_from_fen():
    b = Board()
    b.set_FEN(
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    assert b.position == [2, 3, 4, 5, 6, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7,
                          7, 7, 8, 9, 10, 11, 12, 10, 9, 8]

    b.set_FEN("rnbqkbnr/ppppppPp/8/8/4P3/PP6/2PP1P1P/RNBQKBNR b KQkq - 0 1")
    assert b.position == [2, 3, 4, 5, 6, 4, 3, 2, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7,
                          1, 7, 8, 9, 10, 11, 12, 10, 9, 8]

    b.set_FEN(
        "2b1k1nr/ppp1np1p/4p3/b1N3P1/1P1qP1Q1/P2R4/2N2P1P/RKB2r2 b - - 0 1")
    assert b.position == [2, 6, 4, 0, 0, 8, 0, 0, 0, 0, 3, 0, 0, 1, 0, 1, 1, 0,
                          0, 2, 0, 0, 0, 0, 0, 1, 0, 11, 1, 0, 5, 0, 10, 0, 3,
                          0, 0, 0, 1, 0, 0, 0, 0, 0, 7, 0, 0, 0, 7, 7, 7, 0, 9,
                          7, 0, 7, 0, 0, 10, 0, 12, 0, 9, 8]


def test_pawn_get_legal_moves():
    b = Board()

    # test white straight advance moves
    b.set_FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    assert arr_string(Pawn.get_legal_moves(b, 8)) == ['8 -> 16', '8 -> 24']

    b.set_FEN("rnbqkbnr/pppppppp/8/8/8/P7/1PPPPPPP/RNBQKBNR w KQkq - 0 1")
    assert arr_string(Pawn.get_legal_moves(b, 15)) == ['15 -> 23', '15 -> 31']

    b.set_FEN("rnbqkbnr/pppppppp/8/8/8/P7/1PPPPPPP/RNBQKBNR w KQkq - 0 1")
    assert arr_string(Pawn.get_legal_moves(b, 16)) == ['16 -> 24']

    b.set_FEN("rnbqkbnr/pppppppp/8/8/8/7P/PPPPPPP1/RNBQKBNR w KQkq - 0 1")
    assert arr_string(Pawn.get_legal_moves(b, 23)) == ['23 -> 31']

    # test black straight advance moves
    b.set_FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    assert arr_string(Pawn.get_legal_moves(b, 48)) == ['48 -> 40', '48 -> 32']

    b.set_FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    assert arr_string(Pawn.get_legal_moves(b, 55)) == ['55 -> 47', '55 -> 39']

    b.set_FEN("rnbqkbnr/1ppppppp/p8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    assert arr_string(Pawn.get_legal_moves(b, 40)) == ['40 -> 32']

    b.set_FEN("rnbqkbnr/ppppppp1/7p/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    assert arr_string(Pawn.get_legal_moves(b, 47)) == ['47 -> 39']

    # test taking moves
    b.set_FEN("rnbqkbnr/pppp1ppp/8/4p3/5P2/8/PPPPP1PP/RNBQKBNR w KQkq - 0 1")
    assert arr_string(Pawn.get_legal_moves(b, 29)) == ['29 -> 37', '29 -> 36']


    # print(arr_string(Pawn.get_legal_moves(b, 29)))
