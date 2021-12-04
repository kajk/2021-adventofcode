#! /usr/bin/env python3
import re

from colorama import Fore, Style


class BingoField:

    def __init__(self, num: int):
        self.marked = False
        self.number = num

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.marked:
            return Fore.CYAN + str(self.number) + Style.RESET_ALL
        else:
            return str(self.number)


class BingoBoard:
    def __init__(self, board):
        self.elements = [[BingoField(int(e.strip())) for e in re.compile("[ ]+").split(line)] for line in board]
        # assumption: each bingo line has the same length
        self._line_format = ''
        for e in range(len(self.elements[0])):
            self._line_format += '{' + str(e) + ':2} '

    def _yield_fields(self):
        for line in self.elements:
            for field in line:
                yield field

    @property
    def sum_unmarked(self):
        result = 0
        for field in self._yield_fields():
            if not field.marked:
                result += field.number
        return result

    def mark_draw(self, draw: int):
        for field in self._yield_fields():
            if field.number == draw:
                field.marked = True
                return

    def has_won(self):
        # check lines
        if self._check_board_lines(self.elements):
            return True
        # check columns
        columns = [list(range(len(self.elements))) for _ in range(len(self.elements[0]))]
        for col_idx, line in enumerate(self.elements):
            for row_idx, elm in enumerate(line):
                columns[row_idx][col_idx] = elm
        if self._check_board_lines(columns):
            return True
        return False

    @staticmethod
    def _check_board_lines(lines):
        for line in lines:
            if all(field.marked for field in line):
                return True
        return False

    def __str__(self):
        result = ''
        for line in self.elements:
            result += self._line_format.format(*[str(elm) for elm in line]) + '\n'
        return result


class BingoGame:
    def __init__(self, draw: str):
        self.number_draw: list[int] = [int(e) for e in draw.split(',')]
        self.boards: list[BingoBoard] = []

    def add_board(self, board: BingoBoard):
        self.boards.append(board)

    def play(self):
        for idx, num in enumerate(self.number_draw):
            winner_idx = None
            for b_idx, board in enumerate(self.boards):
                board.mark_draw(num)
                if board.has_won():
                    winner_idx = b_idx
            self.print_state(draw_idx=idx)
            if winner_idx is not None:
                print(f'We have a winner!! {winner_idx}')
                print(f'Result: {self.boards[winner_idx].sum_unmarked} -> {self.boards[winner_idx].sum_unmarked * num}')
                return
            print('----------------')

    def print_state(self, draw_idx=0):
        for idx, num in enumerate(self.number_draw):
            if idx <= draw_idx:
                print('*', end='')
            print(num, end=' ')
        print()
        print()
        for b in self.boards:
            print(str(b))
            print(b.has_won())


def read_input(filename: str) -> BingoGame:
    with open(filename) as fp:
        lines = [line.strip() for line in fp.readlines()]
        game = BingoGame(lines[0])
        board_lines = []
        for line in lines[2:]:  # skip the first 2 lines (draws + empty line)
            if line == '':
                board = BingoBoard(board_lines)
                game.add_board(board)
                board_lines = []
            else:
                board_lines.append(line)
        if len(board_lines) > 0:
            board = BingoBoard(board_lines)
            game.add_board(board)
    return game


def main():
    game = read_input('test.input')
    game.play()


if __name__ == '__main__':
    main()
