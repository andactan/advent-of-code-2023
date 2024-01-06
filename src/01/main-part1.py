import os
from utils import NUMS_ARR


def solve():
    with open(os.path.join(os.getcwd(), "day-01", "input-part1.txt"), "r") as handle:
        retval = 0
        while x := handle.readline().strip():
            length = len(x)
            start = 0
            end = length - 1

            while x[start] not in NUMS_ARR:
                start += 1

            while x[end] not in NUMS_ARR:
                end -= 1

            retval += int(x[start]) * 10 + int(x[end])

        return retval


if __name__ == "__main__":
    print(solve())
