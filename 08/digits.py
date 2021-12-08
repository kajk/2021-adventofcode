#! /usr/bin/env python3

import re
from collections import Counter
from typing import Iterable


def yield_file(filename: str) -> Iterable[str]:
    with open(filename) as fp:
        for line in fp:
            yield line.strip()


def rm(src: str, e: Iterable) -> str:
    res = src
    for remove in e:
        res = res.replace(remove, '')
    return res


class DigitsLine:
    def __init__(self):
        self.inputs = {}
        self.values = {}

    def add_input_element(self, elm: str):
        idx = len(elm)
        value = self._sort(elm)
        if idx in self.inputs:
            self.inputs[idx].append(value)
        else:
            self.inputs[idx] = [value]

    def determine_values(self):
        a = b = c = d = e = f = g = ''
        # length 2 (only 1)
        c = f = self.inputs[2][0]
        # length 3 (only 1)
        a = rm(self.inputs[3][0], c)
        # length 4 (only 1)
        b = d = rm(self.inputs[4][0], c)
        # length 7 (only 1)
        e = g = rm(self.inputs[7][0], a + c + b)
        # length 6 (2 entries)
        missing_options = self._find_missing(self.inputs[6][0])
        missing_options.append(*self._find_missing(self.inputs[6][1]))
        if missing_options[0] in c:
            c = missing_options[0]
            f = rm(f, c)
            g = missing_options[1]
            e = rm(e, g)
        else:
            c = missing_options[1]
            f = rm(f, c)
            e = missing_options[0]
            g = rm(g, e)
        # length 5 (4 entries) --> not resolved: b und d
        all_b_ds = ''.join(re.findall('[' + b + ']', ''.join(self.inputs[5])))
        counts = Counter(all_b_ds)
        if counts[b[0]] == 3:
            d = b[0]
            b = b[1]
        else:
            d = b[1]
            b = b[0]
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
        print(f'''
 {a*4}
{b}    {c}
{b}    {c}
 {d*4}
{e}    {f}
{e}    {f}
 {g*4}''')

    @staticmethod
    def _sort(value: str) -> str:
        return ''.join(sorted(value))

    def parse_value(self, value: str) -> int:
        return self.values[self._sort(value)]

    @staticmethod
    def _find_missing(value: str):
        missing = []
        for v in 'abcdefg':
            if v not in value:
                missing.append(v)
        return missing


def main():
    # TODO: Not for each digit a value is given in the input!!!
    for line in yield_file('test.input'):
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


if __name__ == '__main__':
    main()
