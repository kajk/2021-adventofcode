
from typing import Any, Iterable
from colorama import Fore, Style


def all_lines(filename: str) -> list[str]:
    with open(filename) as fp:
        return [line.strip() for line in fp.readlines()]


def yield_file(filename: str) -> Iterable[str]:
    with open(filename) as fp:
        for line in fp:
            yield line.strip()


def color(value: Any):
    return Fore.CYAN + str(value) + Style.RESET_ALL

