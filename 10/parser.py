#! /usr/bin/env python3.9

from typing import Iterable
from colorama import Fore, Style
from shared import yield_file, color


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


def main():
    SCORE_MAP = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    scores = []
    for line in yield_file('input'):
        chunks = []
        # print(line)
        for elm in line:
            if elm in ['(', '[', '{', '<']:
                chunks.append(Chunk(elm))
            else:
                if chunks[-1].is_valid_closing(elm):
                    del chunks[-1]
                else:
                    chunks = []
                    break
        if len(chunks) > 0:
            completion = ''.join(c.expected_closing for c in reversed(chunks))
            score = 0
            for e in completion:
                score = (score * 5) + SCORE_MAP[e]
            print(f'{color(line)}  - Complete by adding {color(completion)}. {score=}')
            scores.append(score)
    result = sorted(scores)[int(len(scores) / 2)]
    print(f'{result=}')


def main_part1():
    SCORE_MAP = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
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
