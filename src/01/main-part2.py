import os
import re
from utils import NUMS_ARR, NUM_STR_ARR, NUMS_MAP, NUMS_STR_MAP


def solve():
    with open(os.path.join(os.getcwd(), "day-01", "input-part2.txt"), "r") as handle:
        retval = 0
        pattern = f'(?=({"|".join(NUMS_ARR + NUM_STR_ARR)}))'
        
        while x := handle.readline().strip():
            matches = re.findall(pattern, x)
            first = matches[0]
            last = matches[-1]
            m = {**NUMS_MAP, **NUMS_STR_MAP}
            retval += m[first] * 10 + m[last]

        return retval


if __name__ == "__main__":
   print(solve())
