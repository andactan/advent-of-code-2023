import numpy as np
import hashlib

from time import time
from mypackage_sina import read_file


def tilt(lines):
    boundary = [-1 for _ in range(len(lines[0]))]
    for i, line in enumerate(lines):
        for j, char_ in enumerate(line):
            if char_ == "#":
                boundary[j] = i

            elif char_ == "O":
                lines[i][j] = '.'
                lines[(boundary[j] + 1)][j] = 'O'
                boundary[j] += 1


with read_file() as handle:
    lines = [list(item) for item in handle.read().splitlines()]
    lines = np.array(lines)

    cache = dict()
    iterations = 1_000_000_000
    num_cycles = 1
    start_cycle = -1
    start = time()
    for i in range(iterations):
        for _ in range(4):
            tilt(lines)
            lines = np.rot90(lines, k=-1)

        h = tuple(map(tuple, lines))
        if h in cache:
            previous_cycle = list(cache.keys()).index(h)
            # previous_cycle = cache[h] 
            num_cycles = i - previous_cycle # how many cycles until recurring point
            break
        else:
            cache.setdefault(h, np.copy(lines))

    extra = ((iterations - i - 1) % num_cycles)
    cache_keys = list(cache.values())
    previous_cycle = i - num_cycles
    lines = cache_keys[previous_cycle + extra]
    print(lines)
    # for _ in range(extra):
    #     for _ in range(4):
    #         tilt(lines)
    #         lines = np.rot90(lines, k=-1)

    # store northmost point a rock can roll to while
    # analyzing (that's what she said) each row
    num_rows = len(lines)
    rounded_rocks = 0 
    for i, line in enumerate(lines):
        for j, rock in enumerate(line):
            if rock == "O":
                rounded_rocks += (num_rows - i)

    print(rounded_rocks)
    end = time()
    print(f'took {end-start} sec(s)')
