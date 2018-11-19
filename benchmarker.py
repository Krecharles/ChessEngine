from engine import chess


def test():
    engine = chess.Engine()
    engine.setFEN(chess.DEFAULT_FEN)
    print(engine.get_best_move(4))


setup = """
        from engine import chess
        b = chess.Board()
        b.set_FEN(chess.DEFAULT_FEN)
        from benchmarker import test_get_legal_moves
        """


def test_get_legal_moves(board):
    board.get_legal_moves()


    # print(timeit.timeit("test_get_legal_moves(b)", setup=setup, number=1000))
if __name__ == '__main__':
    import timeit

    print(timeit.timeit("test()", setup="from benchmarker import test",
                        number=20))

# Benchmark results version 1 with DEFAULT_FEN:
"""
    depth = 1: 0.08
    depth = 2: 1.8 - 2.0
    depth = 3: 41 (roo = run only once)
"""
# Benchmark results version 2 with DEFAULT_FEN:
"""
    depth = 1: 0.01
    depth = 2: 0.25 - 0.33
    depth = 3: 6.5 - 8.18
    depth = 4: 137 roo
"""

# Benchmark results version 3 with DEFAULT_FEN:
"""
    depth = 1: 0.01
    depth = 2: 0.23 - 0.27
    depth = 3: 5.2 - 5.5
    depth = 4: 123 roo
"""
