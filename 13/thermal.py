#! /usr/bin/env python3.9

from typing import Tuple
from shared import all_lines, yield_grid, yield_grid_elms, LazyGrid


class Thermal:
    @staticmethod
    def parse_lines(lines: list[str]):
        coordinates = []
        folding = False
        for line in lines:
            print(line)
            if line == '':
                folding = True
                grid = Thermal(coordinates)
                grid.print()
            elif folding:
                instruction = line.replace('fold along ', '')
                cor_type, pos = instruction.split('=')
                grid.fold(cor_type, int(pos))
                grid.print()
                print(f'Visible dots: {grid.visible_dots}')
                # break  # part1: break after first fold
            else:
                col, row = line.split(',')
                coordinates.append((int(row), int(col)))

    def __init__(self, coordinates: list[Tuple[int, int]]):
        self.grid: LazyGrid[bool] = LazyGrid()
        for row, col in coordinates:
            self.grid.set(row, col, True)

    def fold(self, cor_type: str, pos: int):
        if cor_type == 'y':
            self._y_fold(pos)
        else:
            self._x_fold(pos)

    def _y_fold(self, pos: int):
        new_grid: LazyGrid[bool] = LazyGrid()
        print('----')
        for row_idx, col_idx, elm in self.grid.yield_grid():
            if row_idx == pos:
                continue
            new_row = row_idx
            if row_idx > pos:
                new_row = row_idx - ((row_idx - pos) * 2)
            print(f'{row_idx=}->{new_row=} {col_idx=}')
            new_grid.set(new_row, col_idx, new_grid.get(new_row, col_idx) or elm)
        self.grid = new_grid

    def _x_fold(self, pos: int):
        new_grid: LazyGrid[bool] = LazyGrid()
        print('----')
        for row_idx, col_idx, elm in self.grid.yield_grid():
            if col_idx == pos:
                continue
            new_col = col_idx
            if col_idx > pos:
                new_col = col_idx - ((col_idx - pos) * 2)
            print(f'{row_idx=} {col_idx=}->{new_col=}')
            new_grid.set(row_idx, new_col, new_grid.get(row_idx, new_col) or elm)
        self.grid = new_grid

    def print(self, grid=None):
        g = self.grid if grid is None else grid
        for row_idx, col_idx, elm in g.yield_grid():
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
        count = 0
        for _, _, elm in self.grid.yield_grid():
            if elm:
                count += 1
        return count


def main():
    Thermal.parse_lines(all_lines('input'))


if __name__ == '__main__':
    main()
