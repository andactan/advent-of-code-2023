import numpy

from mypackage_sina import read_file
from collections import Counter

with read_file() as handle:
    patterns = [[list(line) for line in item.split("\n")] for item in handle.read().split("\n\n")]
    total = 0
    for pattern in patterns:
        pattern_np = numpy.array(pattern)
        # try to find a horizontal reflection line
        horizontal_reflect = 0
        for i in range(1, len(pattern_np)):
            upper = pattern_np[:i]
            lower = numpy.flip(upper, 0)
            generated = numpy.concatenate((upper, lower))
            end = min(2 * i, len(pattern_np))

            if (Counter((pattern_np[:end] == generated[:end]).flatten())[False] == 1):
                horizontal_reflect = i

        vertical_reflect = 0
        for j in range(1, len(pattern_np[0])):
            left = pattern_np[:, :j]
            right = numpy.flip(left, 1)
            generated = numpy.hstack((left, right))
            end = min(2 * j, len(pattern_np[0]))

            if Counter((pattern_np[:, :end] == generated[:, :end]).flatten())[False] == 1:
                vertical_reflect = j

        total += vertical_reflect + 100 * horizontal_reflect

    print(total)