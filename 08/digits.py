#! /usr/bin/env python3

from typing import Iterable


def yield_file(filename: str) -> Iterable[str]:
    with open(filename) as fp:
        for line in fp:
            yield line.strip()


def main():
    result = 0
    for line in yield_file('input'):
        output_values = False
        nums_1478 = 0
        for elm in line.split(' '):
            if elm == '|':
                output_values = True
            elif output_values:
                if len(elm) in [2,4,3,7]:
                    nums_1478 += 1
        print(f'{line}  ---> {nums_1478}')
        result += nums_1478
    print(f'{result=}')



if __name__ == '__main__':
    main()
