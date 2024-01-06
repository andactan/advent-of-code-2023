from mypackage_sina import read_file
from collections import defaultdict


def drop_invalid_cells(table, coors, limit_x, limit_y):
    pipes = {
        "|": lambda x: set([(x[0]-1, x[1]), (x[0]+1, x[1])]),
        '-': lambda x: set([(x[0], x[1]-1), (x[0], x[1]+1)]),
        'F': lambda x: set([(x[0]+1, x[1]), (x[0], x[1]+1)]),
        'L': lambda x: set([(x[0]-1, x[1]), (x[0], x[1]+1)]),
        'J': lambda x: set([(x[0]-1, x[1]), (x[0], x[1]-1)]),
        '7': lambda x: set([(x[0]+1, x[1]), (x[0], x[1]-1)]),
    }

    connection_types = {
        "|": {"north": "|F7S", "south": "|LJS"},
        "-": {"west": "-LFS", "east": "-J7S"},
        "F": {"east": "-J7S", "south": "|LJS"},
        "L": {"north": "|F7S", "east": "-J7S"},
        "J": {"north": "|F7S", "west": "-FLS"},
        "7": {"south": "|LJS", "west": "-FLS"}
    }

    temp = []
    for item in pipes.get(cell)(coors):
        x, y = item
        if (x >= limit_x or
            x < 0 or
            y >= limit_y or
            y < 0 or
            table[x][y] == '.'):
            continue
        
        curr_x, curr_y = coors
        curr_pipe = table[curr_x][curr_y]
        
        if curr_x - x == -1:
            direction = 'south'
        elif curr_x - x == 1:
            direction = 'north'
        elif curr_y - y == -1:
            direction = 'east'
        else:
            direction = 'west'

        item_pipe = table[x][y]
        possible_connections = connection_types[curr_pipe][direction]
        if item_pipe in possible_connections:
            temp.append((x, y))

    return temp

with read_file() as handle:
    lines = handle.read().splitlines()
    adj_list = defaultdict(set)
    rows = len(lines)
    cols = len(lines[0])
    start = None

    for i in range(rows):
        for j in range(cols):
            cell = lines[i][j]
            if not cell == '.':
                if cell == 'S':
                    start = (i, j)
                    continue

                valid_neighbors = drop_invalid_cells(lines, (i, j), rows, cols)
                if valid_neighbors:
                    adj_list[(i, j)].update(valid_neighbors)

                    for n in valid_neighbors:
                        adj_list[n].add(tuple((i, j)))

    queue = [start]
    distances = defaultdict(int)
    distances[start] = 0
    visited = set()
    max_distance = 0
    while queue:
        temp = queue.pop(0)
        distance = distances[temp]
        visited.add(temp)
        
        for item in adj_list[temp]:
            if item not in visited:
                queue.append(item)
                distances[item] = distance + 1

        max_distance = max(max_distance, distance)

    # For shoelace, find corner points
    queue = [start]
    visited = list()
    while queue:
        temp = queue.pop(0)
        visited.append(temp)

        for item in adj_list[temp]:
            if item not in visited:
                queue.append(item)
                break # add one and leave

    # calculate the enclosed area
    area = 0
    visited.append(visited[0])
    for item1, item2 in zip(visited[:-1], visited[1:]):
        area += item1[0] * item2[1] - item2[0] * item1[1]

    area = int(0.5 * abs(area))
    
    # now use Pick's theorem -> area = interior + 0.5 * boundary - 1
    # boundary = max_distance * 2
    # interior = area + 1 - max_distance
    print(area + 1 - max_distance)



