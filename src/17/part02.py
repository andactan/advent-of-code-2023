import heapq
import copy
import numpy as np

from mypackage_sina import read_file
from collections import defaultdict
from time import time
from pprint import pprint


with read_file() as handle:
    lines = np.array([list(map(int, list(line))) for line in handle.read().splitlines()])
    neighbors = {
        "n": [(np.array([-1, 0]), "n"), (np.array([0, 1]), "e"), (np.array([0, -1]), "w")],
        "e": [(np.array([-1, 0]), "n"), (np.array([1, 0]), "s"), (np.array([0, 1]), "e")],
        "s": [(np.array([1, 0]), "s"), (np.array([0, 1]), "e"), (np.array([0, -1]), "w")],
        "w": [(np.array([0, -1]), "w"), (np.array([1, 0]), "s"), (np.array([-1, 0]), "n")]
    }

    valid_turns = {
        "n": np.array([-4, 0]),
        "e": np.array([0, 4]),
        "s": np.array([4, 0]),
        "w": np.array([0, -4])
    }

    is_valid = lambda x: 0 <= x[0] < len(lines) and 0 <= x[1] < len(lines[0])

    # run Dijkstra's
    start_set = [((lines[(0,1)]), 1, "e", (0, 1)), ((lines[(1, 0)]), 1, "s", (1, 0))]
    distances = defaultdict(lambda: float("inf"))
    distances.update(dict([(item[-1], item[0]) for item in start_set]))
    visited = set()
    queue = copy.deepcopy(start_set)
    heapq.heapify(queue)

    while queue:
        distance, so_far, direction, coors = heapq.heappop(queue)
        
        if (*coors, direction, so_far) in visited:
            continue

        visited.add((*coors, direction, so_far))
        np_coors = np.array(coors)
        for n_extra, n_direction in neighbors[direction]:
            if n_direction == direction and so_far == 10:
                continue

            if n_direction != direction and so_far < 4:
                continue

            n = tuple((n_extra + np_coors).tolist())
            if not (is_valid(n)):
                continue

            if n_direction != direction:
                end = valid_turns[n_direction] + np_coors
                if not is_valid(end):
                    continue

            so_far_inner = so_far + 1 if n_direction == direction else 1
            
            weight = (lines[n]) + distance
            if weight < distances[n]:
                distances[n] = weight

            payload = (weight, so_far_inner, n_direction, n)
            heapq.heappush(queue, payload)

    print(distances[(len(lines) - 1, len(lines[0]) - 1)])