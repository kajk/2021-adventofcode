#! /usr/bin/env python3

from typing import Iterable


def yield_file(filename: str) -> Iterable[str]:
    with open(filename) as fp:
        for line in fp:
            yield line.strip()


class Submarine:
    depth: int = 0
    h_pos: int = 0
    aim: int = 0

    def forward(self, value: int):
        self.h_pos += value
        self.depth += self.aim * value

    def up(self, value: int):
        self.aim -= value

    def down(self, value: int):
        self.aim += value

    @property
    def status(self):
        return f'h_pos={self.h_pos:8} depth={self.depth:8} aim={self.aim:8}'

    @property
    def result(self):
        return self.depth * self.h_pos


def run_line(sub: Submarine, line: str):
    tokens = line.split(' ')
    if len(tokens) < 1:
        raise RuntimeException(f'not enough tokens: {line}')
    if tokens[0] == 'forward':
        if len(tokens) != 2:
            raise RuntimeException(f'Expected 2 tokens for "forward": {line}')
        sub.forward(int(tokens[1]))
        return

    if tokens[0] == 'down':
        if len(tokens) != 2:
            raise RuntimeException(f'Expected 2 tokens for "down": {line}')
        sub.down(int(tokens[1]))
        return

    if tokens[0] == 'up':
        if len(tokens) != 2:
            raise RuntimeException(f'Expected 2 tokens for "up": {line}')
        sub.up(int(tokens[1]))
        return

    raise RuntimeException(f'Unexpected first token "{token[0]}" on line "{line}"')
    

def main():
    sub = Submarine()
    for line in yield_file('input'):#('test.input'):
        run_line(sub, line)
        print(f'{line:20} :: {sub.status}')
    print(sub.status)
    print(sub.result)


if __name__ == "__main__":
    main()
