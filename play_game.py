from gameparts import TicTacToe
from gameparts import FieldIndexError

results = open('result.txt', 'r')
team_O = 0
team_X = 0



def main():
    game = TicTacToe()
    game.show_board()
    while True:
        row = int(input("Enter row: "))
        if row > 2 and row > 0:
            raise FieldIndexError
        column = int(input("Enter column: "))
        if column > 2 and column > 0:
            raise FieldIndexError
        game.make_move(row, column)
        game.show_board()
        text, flag = game.check_winner()
        print(text)
        if flag:
            game.show_board()


if __name__ == '__main__':
    main()