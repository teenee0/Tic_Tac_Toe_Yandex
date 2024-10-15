from GameClass import TicTacToe
game = TicTacToe()
game.show_board()
while True:
    game.make_move(int(input()), int(input()))
    game.show_board()
    print(game.check_winner())