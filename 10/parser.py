#! /usr/bin/env python3

from typing import Iterable
from colorama import Fore, Style

def yield_file(filename: str) -> Iterable[str]:
    with open(filename) as fp:
        for line in fp:
            yield line.strip()


class Chunk:
    def __init__(self, char: str):
        if char not in ['(', '[', '{', '<']:
            raise RuntimeException(f'Unexpected {char=}')
        self.char = char

    def is_valid_closing(self, char):
        return self.expected_closing == char

    @property
    def expected_closing(self):
        if self.char == '(':
            return ')'
        if self.char == '[':
            return ']'
        if self.char == '{':
            return '}'
        if self.char == '<':
            return '>'


def color(value: str):
    return Fore.CYAN + value + Style.RESET_ALL


SCORE_MAP = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
}

def main():
    result = 0
    for line in yield_file('input'):
        chunks = []
        for elm in line:
            if elm in ['(', '[', '{', '<']:
                chunks.append(Chunk(elm))
            else:
                if chunks[-1].is_valid_closing(elm):
                    del chunks[-1]
                else:
                    print(f'{color(line)} - Expected {color(chunks[-1].expected_closing)}, but found {color(elm)} instead.')
                    result += SCORE_MAP[elm]
                    break
    print(f'{result=}')
        

if __name__ == '__main__':
    main()
