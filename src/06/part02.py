import re
import math
from mypackage_sina import read_file


with read_file() as handle:
    lines = handle.read().splitlines()

    # 1st line: time, 2nd line: distance to beat
    time_pattern = r'Time:\s+(?P<match>([0-9]+\s*)+)'
    dist_pattern = r'Distance:\s+(?P<match>([0-9]+\s*)+)'

    times = [
        item 
        for item in re.match(time_pattern, lines[0]).groupdict().get("match").split(" ") 
        if item != " " and item != ""
    ]
    distances = [
        item 
        for item in re.match(dist_pattern, lines[1]).groupdict().get("match").split(" ") 
        if item != " " and item != ""
    ]

    time = int("".join(times))
    distance = int("".join(distances))

    root1 = math.ceil((time - math.sqrt(time ** 2 - 4 * distance)) / 2)
    root2 = math.floor((time + math.sqrt(time ** 2 - 4 * distance)) / 2)
    
    if (time - root1) * root1 == distance:
        root1 += 1

    if (time - root2) * root2 == distance:
        root2 -= 1
    
    
    winning_ways = (root2 - root1 + 1)

    print(time, distance, root1, root2)

    print(winning_ways)