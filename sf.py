from stockfish import Stockfish

path = 'G:\My Drive\Python\ChessEngine\stockfish-9-win\Windows\stockfish_9_x32.exe'
# path = '/Users/charelkremer/Documents/Coding/Python/lib/stockfish/stockfish-9-64'
params = {
    # "Minimum Thinking Time": 5000,  # in milliseconds
    "Hash": 512,  # in MB
    "Threads": 2,
}
stockfish = Stockfish(path, depth=10, param=params)



# # set position by moves:
# stockfish.set_position(['e2e4', 'e7e6'])
#
# # set position by FEN:
# stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")
#
# print("begin calculation")
# print(stockfish.get_best_move()) # d2d4
