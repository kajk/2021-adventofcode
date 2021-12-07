#! /usr/bin/env python3


def calculate_fuel_requirement(crab_positions, target) -> int:
    total_fuel = 0
    for crab in crab_positions:
        total_fuel += abs(crab - target)
    return total_fuel


def brute_force_result(crab_positions) -> int:
    most_efficient_target = None
    most_efficient_fuel_usage = None
    for target in range(min(crab_positions), max(crab_positions) + 1):
        fuel = calculate_fuel_requirement(crab_positions, target)
        if most_efficient_target is None or fuel < most_efficient_fuel_usage:
            most_efficient_target = target
            most_efficient_fuel_usage = fuel
        print(f'{target} -> Fuel: {fuel}  (Efficient={most_efficient_target:})')
    return most_efficient_target


def main():
    with open('test.input') as fp:
        crab_positions = [int(elm.strip()) for elm in fp.readline().split(',')]
        result = brute_force_result(crab_positions)
        print(f'cheapest possible outcome: {result}')

if __name__ == '__main__':
    main()
