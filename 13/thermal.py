#! /usr/bin/env python3.9

from typing import Tuple
from shared import all_lines, yield_grid, yield_grid_elms


class Grid:
    @staticmethod
    def parse_lines(lines: list[str]):
        coordinates = []
        max_row = 0
        max_col = 0
        folding = False
        for l in lines:
            print(l)
            if l == '':
                folding = True
                grid = Grid(max_row, max_col, coordinates)
                grid.print()
            elif folding:
                instruction = l.replace('fold along ', '')
                cor_type, pos = instruction.split('=')
                grid.fold(cor_type, int(pos))
                grid.print()
                print(f'Visible dots: {grid.visible_dots}')
                break  # part1: break after first fold
            else:
                s = l.split(',')
                col = int(s[0])
                row = int(s[1])
                coordinates.append((row, col))
                if row > max_row:
                    max_row = row
                if col > max_col:
                    max_col = col

    def __init__(self, max_row: int, max_col: int, coordinates: list[Tuple[int, int]]):
        self.coordinates = [[False for _ in range(max_col + 1)] for _ in range(max_row + 1)]
        for row, col in coordinates:
            self.coordinates[row][col] = True

    def fold(self, cor_type: str, pos: int):
        if cor_type == 'y':
            self._y_fold(pos)
        else:
            print('No')

    def _y_fold(self, pos: int):
        new_coordinates = [[False for _ in range(len(self.coordinates[0]))] for _ in range(int(len(self.coordinates) / 2))]
        self.print(new_coordinates)
        print('----')
        for row_idx, col_idx, elm in yield_grid(self.coordinates):
            if row_idx == pos:
                continue
            new_row = row_idx
            if row_idx > pos:
                new_row = row_idx - ((row_idx - pos) * 2)
            print(f'{row_idx=}->{new_row=} {col_idx=}')
            new_coordinates[new_row][col_idx] = new_coordinates[new_row][col_idx] or elm
        self.coordinates = new_coordinates

    def print(self, cor = None):
        for row_idx, col_idx, elm in yield_grid(self.coordinates if cor is None else cor):
            if col_idx == 0 and row_idx != 0:
                print()
            if col_idx == 0:
                print(f'[{row_idx}] ', end='')
            if elm:
                print('#', end='')
            else:
                print('.', end='')
        print()

    @property
    def visible_dots(self):
        c = 0
        for elm in yield_grid_elms(self.coordinates):
            if elm:
                c += 1
        return c


def main():
    Grid.parse_lines(all_lines('test.input'))


if __name__ == '__main__':
    main()
