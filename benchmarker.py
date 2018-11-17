from engine import chess
def test():
    engine = chess.Engine()
    engine.setFEN(chess.DEFAULT_FEN)
    print(engine.get_best_move(3))


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from benchmarker import test", number=20))


# Benchmark results version 1 with DEFAULT_FEN:
"""
    depth = 1: 0.08
    depth = 2: 1.8 - 2.0
    depth = 3: 41
"""