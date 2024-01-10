import heapq
import copy
import numpy as np

from mypackage_sina import read_file
from collections import defaultdict
from time import time


with read_file() as handle:
    lines = np.array([list(line) for line in handle.read().splitlines()])
    neighbors = {
        "n": [(np.array([-1, 0]), "n"), (np.array([0, 1]), "e"), (np.array([0, -1]), "w")],
        "e": [(np.array([-1, 0]), "n"), (np.array([1, 0]), "s"), (np.array([0, 1]), "e")],
        "s": [(np.array([1, 0]), "s"), (np.array([0, 1]), "e"), (np.array([0, -1]), "w")],
        "w": [(np.array([0, -1]), "w"), (np.array([1, 0]), "s"), (np.array([-1, 0]), "n")]
    }
    is_valid = lambda x: 0 <= x[0] < len(lines) and 0 <= x[1] < len(lines[0])

    # run Dijkstra's
    start_set = [(int(lines[(0,1)]), 2, "e", (0, 1)), (int(lines[(1, 0)]), 2, "s", (1, 0))]
    distances = defaultdict(lambda: float("inf"))
    distances.update(dict([(item[-1], item[0]) for item in start_set]))
    visited = set()
    queue = copy.deepcopy(start_set)
    heapq.heapify(queue)

    max_queue_size = len(queue)
    start = time()
    while queue:
        max_queue_size = max(max_queue_size, len(queue))
        distance, remaining, direction, coors = heapq.heappop(queue)
        
        if (*coors, direction, remaining) in visited:
            continue

        visited.add((*coors, direction, remaining))
        np_coors = np.array(coors)
        for n_extra, n_direction in neighbors[direction]:
            n = tuple((n_extra + np_coors).tolist())
            if not is_valid(n):
                continue

            remaining_temp = remaining - 1 if n_direction == direction else 2
            if remaining_temp == -1:
                continue

            if (*n, n_direction, remaining_temp) in visited:
                continue
            
            weight = int(lines[n]) + distance
            if weight < distances[n]:
                distances[n] = weight

            payload = (weight, remaining_temp, n_direction, n)
            heapq.heappush(queue, payload)

    end = time()
    print(end-start)
    print(max_queue_size)
    print(distances[(len(lines) - 1, len(lines[0]) - 1)])






