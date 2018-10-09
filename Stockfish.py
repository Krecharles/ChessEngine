from stockfish import Stockfish

stockfish = Stockfish('G:\My Drive\Python\ChessEngine\stockfish-9-win\Windows\stockfish_9_x32.exe')

# set position by moves:
stockfish.set_position(['e2e4', 'e7e6'])

# set position by FEN:
stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")

print(stockfish.get_best_move()) # d2d4
print(stockfish.is_move_correct('a2a3')) # True
