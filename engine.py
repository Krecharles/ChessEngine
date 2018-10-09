from stockfish import Stockfish

stockfish = Stockfish('/Users/charelkremer/Documents/Coding/Python/lib/stockfish/stockfish-9-64')

# # set position by moves:
# stockfish.set_position(['e2e4', 'e7e6'])
#
# # set position by FEN:
# stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")
#
# print("begin calculation")
# print(stockfish.get_best_move()) # d2d4