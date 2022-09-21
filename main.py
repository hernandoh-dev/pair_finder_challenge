import os
import sys
import argparse
import datetime
from typing import Set, Tuple


def main(arguments: argparse.Namespace):
    """
    Core function.
    :param arguments: Script parameters.
    """

    numbers = list(sorted(map(lambda x: int(x), arguments.numbers)))
    numbers_size = len(numbers)
    if 10000 >= numbers_size > sys.getrecursionlimit() or arguments.unlimit:
        sys.setrecursionlimit(len(numbers) + 1)

    init = datetime.datetime.now()
    message = "at least 2 values are required to carry out the process"
    if numbers_size > 1:
        pairs = set()
        find_pairs(numbers, pairs, arguments.target)
        print(pairs)
        message = f"\nTook {datetime.datetime.now() - init} for {numbers_size} numbers."

    print(message)


def find_pairs(numbers: list, pairs: Set[Tuple[int, int]], target: int):
    """
    Given an unsorted array, find recursively all pairs with the given sum in it.
    (Own version)
    :param numbers: list of numbers Ie, [2,3,5,7,1]
    :param pairs: set of pairs of numbers.
    :param target: Given sum.
    :return:
    """
    if not numbers:
        return pairs
    current: int = numbers.pop(0)
    pair_list: list = list(filter(lambda x: target - current == x, numbers))
    if pair_list:
        pair: int = pair_list.pop(0)
        numbers.remove(pair)
        result: tuple = tuple(sorted([current, pair]))
        pairs.add(result)

    return find_pairs(numbers, pairs, target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Returns the pairs from a list that sum to a given value.",
        usage=f"""
            This script iterates a list of up to 10,000 integers
            to find all pairs with the given sum in it.

            If you want to process more, it is possible to overload the ram memory.

            run ```python main.py``` --help for more info.
            """,
    )
    parser.add_argument(
        "--target",
        type=int,
        help="Comparative value to select the pair of values from list.",
        required=True,
    )
    parser.add_argument(
        "--numbers",
        type=str,
        nargs="+",
        help="Set of non duplicate integers.",
        required=True,
    )

    parser.add_argument(
        "--unlimit",
        type=bool,
        help="Defines if process a list larger than 10.000 items.",
        default=False
    )

    args = parser.parse_args()
    main(args)
