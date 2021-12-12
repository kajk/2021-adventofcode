#! /usr/bin/env python3.9

from typing import Iterable, Tuple
from shared import yield_file


class Cave:
    def __init__(self, name: str):
        self.name = name
        self.edges: set[Cave] = set()

    @property
    def is_big(self):
        return self.name.isupper()

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


def build_cave_system(filename: str) -> Tuple[Cave, Cave]:
    caves = {}
    start = Cave('start')
    end = Cave('end')
    caves = {'start': start, 'end': end}
    for line in yield_file(filename):
        src, target = line.split('-')
        src_cave = caves.get(src, Cave(src))
        caves[src] = src_cave
        target_cave = caves.get(target, Cave(target))
        caves[target] = target_cave
        src_cave.edges.add(target_cave)
        target_cave.edges.add(src_cave)
    print('All Caves')
    for cave in caves.values():
        print(f'{cave.name}: {",".join(e.name for e in cave.edges)}')
    return start, end


def yield_options(cave: Cave, path: list[Cave], visited_small_twice: bool) -> Iterable[Cave]:
    for e in cave.edges:
        if e.name == 'start':
            continue
        if e.is_big or not visited_small_twice or e not in path:
            print(f'{e} -> {path=}')
            yield e


def find_paths(cave: Cave, path: list[Cave], visited_small_twice: bool = False) -> Iterable[list[Cave]]:
    for option in yield_options(cave, path, visited_small_twice):
        if option.name == 'end':
            yield path + [option]
        else:
            new_visited_small_twice = visited_small_twice
            if not visited_small_twice and not option.is_big and option in path:
                new_visited_small_twice = True
            yield from find_paths(option, path + [option], new_visited_small_twice)


def find_all_paths_part1(start: Cave) -> Iterable[list[Cave]]:
    for edge in start.edges:
        yield from find_paths(edge, [start, edge], True)


def find_all_paths_part2(start: Cave) -> Iterable[list[Cave]]:
    for edge in start.edges:
        yield from find_paths(edge, [start, edge])


def main():
    start, _ = build_cave_system('input')
    paths = list(find_all_paths_part2(start))
    for p in paths:
        print(f'{",".join(e.name for e in p)}')
    print(f'Number of caves: {len(paths)}')


if __name__ == '__main__':
    main()
