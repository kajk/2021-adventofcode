#! /usr/bin/env python3

from itertools import islice

def yield_input_window_sum():
    with open('input') as fp:
        values = [int(line.strip()) for line in fp]
        for idx in range(0, len(values) - 2):
            print(f'{idx}:{values[idx]} {idx+1}:{values[idx+1]} {idx+2}:{values[idx+2]}', end=':: ')
            yield values[idx] + values[idx+1]  + values[idx+2]


def main():
    prev_value = None
    increase_count = 0
    for value in yield_input_window_sum():
        if prev_value is None:
            print(f'{value} (N/A - no previous measurement)')
        elif value < prev_value:
            print(f'{value} (decreased)')
        elif value > prev_value:
            print(f'{value} (increased)')
            increase_count += 1
        else:
            print(f'{value} (same)')
        prev_value = value
    print(f'Increase count: {increase_count}')

if __name__ == '__main__':
    main()
