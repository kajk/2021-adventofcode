#! /usr/bin/env python3

from __future__ import annotations

from typing import Iterable


def yield_file(filename: str) -> Iterable[str]:
    with open(filename) as fp:
        for line in fp:
            yield line.strip()


class OccuranceCounter:
    occurances: dict[str, int]

    def __init__(self):
        self.occurances = {}

    def __repr__(self):
        return f'{self.occurances=}\n'

    def increment(self, value):
        self.occurances[value] = self.occurances.get(value, 0) + 1

    @property
    def most_common(self) -> str | None:
        result = None
        occ = None
        for value, count in self.occurances.items():
            if occ is None or count > occ:
                occ = count
                result = value
        return result

    @property
    def least_common(self) -> str | None:
        result = None
        occ = None
        for value, count in self.occurances.items():
            if occ is None or count < occ:
                occ = count
                result = value
        return result


class SubDiagnostics:
    lines_consumed: int = 0
    rate: dict[int, OccuranceCounter] = {}

    def consume_line(self, line: str):
        for idx, value in enumerate(line):
            try:
                counter = self.rate[idx]
            except KeyError:
                counter = OccuranceCounter()
                self.rate[idx] = counter
            counter.increment(value)
            print(f'{counter.occurances=}')
        print(f'{line=} {self.rate=}')

    @property
    def gamma_rate_str(self) -> str:
        rate = ''
        for count in self.rate.values():
            rate = rate + count.most_common
        return rate

    @property
    def gamma_rate(self):
        return int(self.gamma_rate_str, 2)

    @property
    def epsilon_rate_str(self):
        rate = ''
        for count in self.rate.values():
            rate = rate + count.least_common
        return rate

    @property
    def epsilon_rate(self):
        return int(self.epsilon_rate_str, 2)

    @property
    def diagnostics(self):
        return f'gamma_rate={self.gamma_rate_str}/{self.gamma_rate} ' \
               f'epsilon_rate={self.epsilon_rate_str}/{self.epsilon_rate}'

    @property
    def result(self):
        return self.epsilon_rate * self.gamma_rate


def main():
    diag = SubDiagnostics()
    for line in yield_file('input'):
        diag.consume_line(line)
    print(diag.diagnostics)
    print(diag.result)


if __name__ == '__main__':
    main()
