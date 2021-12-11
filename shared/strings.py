
from typing import Iterable


def remove_from_str(src: str, rm: Iterable[str]) -> str:
    res = src
    for remove in rm:
        res = res.replace(remove, '')
    return res
