class TicTacToe:
    '''Класс реалезующий методы для игры в крестики - нолики'''

    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.player = "X"


    def make_move(self, row, col):
        '''Метод реализующий ход игрока, с проверкой занятости клетки'''
        if self.board[row][col] == " ":
            self.board[row][col] = self.player
        else:
            self.switch_player()
            print("Эта клетка занята!")


    def check_winner(self):
        '''Делаает проверку на выйгрыш, на выходе дает строку'''
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] == self.player or
                    self.board[0][i] == self.board[1][i] == self.board[2][i] == self.player):

                self.clear_board()
                return f"{self.player} won"

        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == self.player or
                self.board[0][2] == self.board[1][1] == self.board[2][0] == self.player):

            self.clear_board()
            return f"{self.player} won"

        if " " not in "".join(["".join(row) for row in self.board]):

            self.clear_board()
            return "Ничья"
        else:

            self.switch_player()
            return f"Играем"


    def clear_board(self):
        '''Очищает игровое поле'''
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.player = "X"


    def switch_player(self):
        '''Меняет игроков местами'''
        self.player = "X" if self.player == "O" else "O"


    def show_board(self):
        '''Выводит игровое поле'''
        for row in self.board:
            print('|'.join(row))
            print('_' * 5)

