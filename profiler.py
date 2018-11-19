import cProfile, pstats, io
import chess

engine = chess.Engine()
engine.setFEN(chess.DEFAULT_FEN)

pr = cProfile.Profile()
pr.enable()
retval = engine.get_best_move(4)
pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
