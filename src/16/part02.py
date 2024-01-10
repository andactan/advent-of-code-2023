from mypackage_sina import read_file
from collections import defaultdict
from time import time


def check_point_(x, y, limit_x, limit_y):
    return 0 <= x < limit_x and 0 <= y < limit_y

def next_tile(tile_type, direction):
    relays = {
        '.': {"n": [(-1, 0)], "e": [(0, 1)], "s": [(1, 0)], "w": [(0, -1)]},
        "-": {"n": [(0, -1), (0, 1)], "e": [(0, 1)], "s": [(0, -1), (0, 1)], "w": [(0, -1)]},
        "|": {"n": [(-1, 0)], "e": [(-1, 0), (1, 0)], "s": [(1, 0)], "w": [(-1, 0), (1, 0)]},
        "/": {"n": [(0, 1)], "e": [(-1, 0)], "s": [(0, -1)], "w": [(1, 0)]},
        "\\": {"n": [(0, -1)], "e": [(1, 0)], "s": [(0, 1)], "w": [(-1, 0)]}
    }

    return relays[tile_type][direction]

with read_file() as handle:
    lines = handle.read().splitlines()
    is_valid = lambda x, y: check_point_(x, y, len(lines), len(lines[0]))
    sum_ = lambda x, y: x + y
    directions = {(1, 0): "s", (-1,0): "n", (0, 1): "e", (0, -1): "w"}

    start_positions = (
        [(0, i, "s") for i in range(len(lines[0]))] + 
        [(len(lines), i, "n") for i in range(len(lines[0]))] + 
        [(i, 0, "e") for i in range(len(lines))] +
        [(i, len(lines[0]), "w") for i in range(len(lines))])
    
    max_tiles = -1
    for start_position in start_positions:
        visited = set()
        visited_tiles = set()
        queue = [start_position]
        while queue:
            curr = queue.pop(0)
            x, y, d = curr

            if curr in visited or not is_valid(x, y):
                continue
            
            visited.add(curr)
            visited_tiles.add(curr[:2])
            
            relays = next_tile(lines[x][y], d)
            coors = (x, y)
            for relay in relays:
                next_coors = tuple(map(sum_, coors, relay))
                next_d = directions[relay]
                queue.append((*next_coors, next_d))

        max_tiles = max(max_tiles, len(visited_tiles))

    print(max_tiles)
    


