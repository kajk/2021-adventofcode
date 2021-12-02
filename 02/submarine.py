#! /usr/bin/env python3

from typing import Iterable


def yield_file(filename: str) -> Iterable[str]:
    with open(filename) as fp:
        for line in fp:
            yield line.strip()


class Submarine:
    depth: int = 0
    h_pos: int = 0

    def forward(self, value: int):
        self.h_pos += value

    def up(self, value: int):
        self.depth -= value

    def down(self, value: int):
        self.depth += value

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
    for line in yield_file('input'):
        print(line)
        run_line(sub, line)
    print(sub.result)


if __name__ == "__main__":
    main()
