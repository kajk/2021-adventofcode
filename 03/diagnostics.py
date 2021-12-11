#! /usr/bin/env python3.9

from __future__ import annotations

from typing import Iterable, Callable
from shared import yield_file


class OccurrencesCounter:
    occurrences: dict[str, int]

    def __init__(self):
        self.occurrences = {}

    def __repr__(self):
        return f'{self.occurrences}'

    def increment(self, value):
        self.occurrences[value] = self.occurrences.get(value, 0) + 1

    @property
    def most_common(self) -> str | None:
        result = None
        occ = None
        for value, count in self.occurrences.items():
            if occ is None or count > occ:
                occ = count
                result = value
            elif count == occ:
                result = '1'
        return result

    @property
    def least_common(self) -> str | None:
        result = None
        occ = None
        for value, count in self.occurrences.items():
            if occ is None or count < occ:
                occ = count
                result = value
            elif count == occ:
                result = '0'
        return result


def calculate_occurrences(lines: list[str]) -> dict[int, OccurrencesCounter]:
    rate: dict[int, OccurrencesCounter] = {}
    for line in lines:
        for idx, value in enumerate(line):
            try:
                counter = rate[idx]
            except KeyError:
                counter = OccurrencesCounter()
                rate[idx] = counter
            counter.increment(value)
        print(f'{line=} {rate=}')
    return rate


class SubDiagnostics:
    lines: list[str] = []

    def consume_line(self, line: str):
        self.lines.append(line)

    # part 1

    @property
    def gamma_rate_str(self) -> str:
        rate_value = ''
        rate = calculate_occurrences(self.lines)
        for count in rate.values():
            rate_value = rate_value + count.most_common
        return rate_value

    @property
    def gamma_rate(self):
        return int(self.gamma_rate_str, 2)

    @property
    def epsilon_rate_str(self):
        rate_value = ''
        rate = calculate_occurrences(self.lines)
        for count in rate.values():
            rate_value = rate_value + count.least_common
        return rate_value

    @property
    def epsilon_rate(self):
        return int(self.epsilon_rate_str, 2)

    @property
    def part1_diagnostics(self):
        return f'gamma_rate={self.gamma_rate_str}/{self.gamma_rate} ' \
               f'epsilon_rate={self.epsilon_rate_str}/{self.epsilon_rate}'

    @property
    def part1(self):
        return self.epsilon_rate * self.gamma_rate

    # part 2

    def _filter(self, condition: Callable[[OccurrencesCounter], str]):
        filtered = self.lines
        for idx in range(0, len(self.lines[0])):
            value = calculate_occurrences(filtered)
            most_common = condition(value[idx])
            filtered = [line for line in filtered if line[idx] == most_common]
            print(f'{idx=} {most_common=} lines={filtered}')
            if len(filtered) == 1:
                return filtered[0]

    @property
    def oxygen_generator_rating_str(self):
        return self._filter(lambda c: c.most_common)

    @property
    def oxygen_generator_rating(self):
        return int(self.oxygen_generator_rating_str, 2)

    @property
    def c02_scrubber_rating_str(self):
        return self._filter(lambda c: c.least_common)

    @property
    def c02_scrubber_rating(self):
        return int(self.c02_scrubber_rating_str, 2)

    @property
    def part2_diagnostics(self):
        return f'oxygen_generator_rating={self.oxygen_generator_rating_str}/{self.oxygen_generator_rating} ' \
               f'co2_scrubber_rating={self.c02_scrubber_rating_str}/{self.c02_scrubber_rating}'

    @property
    def part2(self):
        return self.oxygen_generator_rating * self.c02_scrubber_rating


def main():
    diag = SubDiagnostics()
    for line in yield_file('input'):
        diag.consume_line(line)
    print('------')
    print(diag.part1_diagnostics)
    print(diag.part1)
    print('------')
    print(diag.part2_diagnostics)
    print(diag.part2)


if __name__ == '__main__':
    main()
