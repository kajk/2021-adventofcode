
from typing import Any, Iterable


def endless_ints(start = 0) -> Iterable[int]:
    idx = start
    while True:
        yield idx
        idx += 1

def join_list(l: list[Any], sep: str = '') -> str:
    return sep.join(str(elm) for elm in l)
