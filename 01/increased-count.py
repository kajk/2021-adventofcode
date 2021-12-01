#! /usr/bin/env python3


def main():
    with open('input') as fp:
        prev_value = None
        increase_count = 0
        for line in fp:
            value = int(line.strip())
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
