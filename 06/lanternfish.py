#! /usr/bin/env python3

from __future__ import annotations
from typing import Tuple


class NewFish:
    def __init__(self, size: int):
        self.size = size
        self.timer = 8


class FishShool:
    def __init__(self, init: list[int]):
        self.initial_fish = init
        self.new_fish = []

    def pass_shool_day(self):
        new_fish_counter = 0
        for idx, fish in enumerate(self.initial_fish):
            fish_timer, new_fish = pass_day(fish)
            self.initial_fish[idx] = fish_timer
            if new_fish is not None:
                new_fish_counter += 1
        for idx, new_fish in enumerate(self.new_fish):
            fish_timer, new_fish_timer = pass_day(new_fish.timer)
            new_fish.timer = fish_timer
            if new_fish_timer is not None:
                new_fish_counter += new_fish.size
        if new_fish_counter > 0:
            self.new_fish.append(NewFish(new_fish_counter))

    def __len__(self):
        return len(self.initial_fish) + sum(f.size for f in self.new_fish)


def pass_day(fish_timer :int) -> Tuple[int, int | None]:
    fish_timer -= 1
    if fish_timer < 0:
        fish_timer = 6
        return fish_timer, 8
    return fish_timer, None


def next_day(fishes: list[int]) -> list[int]:
    # next_fishes = list(fishes)
    for idx, fish_timer in enumerate(fishes):
        fish_timer, new_fish_timer = pass_day(fish_timer)
        fishes[idx] = fish_timer
        if new_fish_timer is not None:
            fishes.append(new_fish_timer)
    return fishes


def join_int_list(ints: list[int]) -> str:
    return f'{",".join([str(elm) for elm in ints])}'

def main():
    with open('input') as fp:
        input_line = fp.readline().strip()
        fishes = [int(f) for f in input_line.split(',')]
        print(f'Initial state: {join_int_list(fishes)}')
        shool = FishShool(fishes)
        for day in range(1, 256 + 1):
            shool.pass_shool_day()
            print(f'After {day:2} days: {len(shool)}')
        print(f'There are a total of {len(shool)}')


if __name__ == '__main__':
    main()
