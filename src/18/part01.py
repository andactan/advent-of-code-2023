import numpy as np

from mypackage_sina import read_file
from collections import defaultdict


with read_file() as handle:
    directions_map = {
        "0": "R",
        "1": "D",
        "2": "L",
        "3": "U"
    }

    lines = [
        [directions_map[c[-2]], int(c[2: 7], 16), c[1:-1]] 
        for _, _, c in [line.split(" ") 
        for line in handle.read().splitlines()]
    ]

    directions = {
        "R": lambda x: np.array((0, x)),
        "L": lambda x: np.array((0, -x)),
        "U": lambda x: np.array((-x, 0)),
        "D": lambda x: np.array((x, 0)) 
    }
    
    graph = defaultdict(lambda: {"color": None, "next": None})
    curr = np.array((0, 0))
    border_length = 0
    for direction, length, color in lines:
        border_length += length
        next_p = curr + directions[direction](length)
        graph[tuple(curr)]["next"] = tuple(next_p)
        graph[tuple(curr)]["color"] = color

        curr = next_p

    keys = list(graph.keys())
    keys.append(keys[0])

    # again a combination of Pick's and shoelace as in Day 10
    # reminder: Picks -> area = interior + boundary/2 - 1
    total = 0
    for p1, p2 in zip(keys[:-1], keys[1:]):
        # map tuples to int since tuple conversion of numpy arrays conserves underlying data type of int16
        p1_ = tuple(map(int, p1))
        p2_ = tuple(map(int, p2))
        total += p1_[0] * p2_[1] - p1_[1] * p2_[0]

    area = int(abs(total) * 0.5)
    interior_points = area + 1 - border_length // 2

    print(border_length + interior_points)
