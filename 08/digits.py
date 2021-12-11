#! /usr/bin/env python3.9

from collections import Counter
from typing import Iterable
from shared import remove_from_str as rm, yield_file


class DigitsLine:
    def __init__(self):
        self.inputs = {}
        self.values = {}

    def add_input_element(self, elm: str):
        idx = len(elm)
        value = elm  # = self._sort(elm)
        if idx in self.inputs:
            self.inputs[idx].append(value)
        else:
            self.inputs[idx] = [value]

    def determine_values(self):
        # length 2 (only 1)
        c = f = self.inputs[2][0]
        # length 3 (only 1)
        a = rm(self.inputs[3][0], c)
        # length 4 (only 1)
        b = d = rm(self.inputs[4][0], c)
        # length 7 (only 1)
        e = g = rm(self.inputs[7][0], a + c + b)
        # length 5 (3 entries)
        five_counter = Counter(''.join(self.inputs[5]))
        singles = [e for e, _ in filter(lambda v: v[1] == 1, five_counter.items())]
        if singles[0] in b:
            b = singles[0]
            e = singles[1]
        else:
            b = singles[1]
            e = singles[0]
        d = rm(d, b)
        g = rm(g, e)
        # length 6 (3 entries)
        six_counter = Counter(rm(''.join(self.inputs[6]), a + b + d + e))
        c = [e for e, _ in filter(lambda v: v[1] == 2, six_counter.items())][0]
        f = rm(f, c)

        # populate values dict
        self.values[self._sort(a + b + c + e + f + g)] = 0
        self.values[self._sort(c + f)] = 1
        self.values[self._sort(a + c + d + e + g)] = 2
        self.values[self._sort(a + c + d + f + g)] = 3
        self.values[self._sort(b + c + d + f)] = 4
        self.values[self._sort(a + b + d + f + g)] = 5
        self.values[self._sort(a + b + d + e + f + g)] = 6
        self.values[self._sort(a + c + f)] = 7
        self.values[self._sort(a + b + c + d + e + f + g)] = 8
        self.values[self._sort(a + b + c + d + f + g)] = 9
        # print segment
#         print(f'''
#  {a * 4}
# {b}    {c}
# {b}    {c}
#  {d * 4}
# {e}    {f}
# {e}    {f}
#  {g * 4}''')

    @staticmethod
    def _sort(value: str) -> str:
        return ''.join(sorted(value))

    def parse_value(self, value: str) -> int:
        return self.values[self._sort(value)]


def main():
    result = 0
    for line in yield_file('input'):
        digi = DigitsLine()
        res = ''
        output_values = False
        for elm in line.split(' '):
            if elm == '|':
                output_values = True
                digi.determine_values()
            elif not output_values:
                digi.add_input_element(elm)
            else:
                res += str(digi.parse_value(elm))
        print(int(res))
        result += int(res)
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
