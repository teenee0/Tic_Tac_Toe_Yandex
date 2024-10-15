from .CustomErrors import CellOccupiedError

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
            raise CellOccupiedError



    def check_winner(self):
        '''Делаает проверку на выйгрыш, на выходе дает строку'''
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] == self.player or
                    self.board[0][i] == self.board[1][i] == self.board[2][i] == self.player):


                text, flag = self.on_win_method(f"{self.player} won")
                return text, flag

        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == self.player or
                self.board[0][2] == self.board[1][1] == self.board[2][0] == self.player):

            text, flag = self.on_win_method(f"{self.player} won")
            return text, flag

        if " " not in "".join(["".join(row) for row in self.board]):

            text, flag = self.on_win_method("Ничья")
            return text, flag

        else:

            self.switch_player()
            return f"Играем", False


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


    def safe_result(self, result):
        '''Метод логирования выйгрышей'''
        results = open('result.txt', 'a')
        results.write(f"{result}\n")
        results.close()

    def on_win_method(self, text):
        '''Промежуточная функция для обновления поля и сохранения результата'''
        self.safe_result(text)
        self.show_result()
        self.clear_board()
        return f"{text}", True


    def show_result(self):
        '''Выводит резуьтаты игр'''
        results = open('result.txt', 'r')
        team_O = 0
        team_X = 0
        print('_' * 5)
        for line in results:
            print(line, end='')
            if line[0] == "O":
                team_O += 1
            elif line[0] == "X":
                team_X += 1
            else:
                continue
        print('_' * 5)
        print(f"Команда крестиков выйграла: {team_X} раз\n"
              f"Команда ноликов выйграла: {team_O} раз")
        print('_' * 5)







