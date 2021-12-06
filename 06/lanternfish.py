#! /usr/bin/env python3

from __future__ import annotations
from typing import Tuple


def pass_day(fish_timer :int) -> Tuple[int, int | None]:
    fish_timer -= 1
    if fish_timer < 0:
        fish_timer = 6
        return fish_timer, 8
    return fish_timer, None


def next_day(fishes: list[int]) -> list[int]:
    next_fishes = list(fishes)
    for idx, fish_timer in enumerate(fishes):
        fish_timer, new_fish_timer = pass_day(fish_timer)
        next_fishes[idx] = fish_timer
        if new_fish_timer is not None:
            next_fishes.append(new_fish_timer)
    return next_fishes


def join_int_list(ints: list[int]) -> str:
    return f'{",".join([str(elm) for elm in ints])}'

def main():
    with open('test.input') as fp:
        input_line = fp.readline().strip()
        fishes = [int(f) for f in input_line.split(',')]
        print(f'Initial state: {join_int_list(fishes)}')
        for day in range(1, 80 + 1):
            fishes = next_day(fishes)
            print(f'After {day:2} days: {join_int_list(fishes)}')
        print(f'There are a total of {len(fishes)}')


if __name__ == '__main__':
    main()
