import functools

from mypackage_sina import read_file
from collections import Counter

# five -> 7
# four -> 6
# full -> 5
# three -> 4
# twop -> 3
# onep -> 2
# high -> 1
class State:
    def __init__(self, t, *args):
        self.t = t
        self.neighbors = {k: v for v, k in args}

    def next(self, arg):
        return self.neighbors.get(arg)

class StateGraph:
    _graph = {
            7: State(7, (7, 5)),
            6: State(6, (7, 4), (7, 1)),
            5: State(5, (7, 2), (7, 3)),
            4: State(4, (6, 1), (6, 2)),
            3: State(3, (5, 1), (6, 2)),
            2: State(2, (4, 2), (4, 1)),
            1: State(1, (2, 1))
    }

    def get(arg):
        return StateGraph._graph.get(arg)


def type_checker(arg):
    counts = Counter(arg)
    l = len(counts)
    dirty = 0
    rank = -1

    if "J" in counts:
        dirty = counts.get("J")

    if l == 1:
        rank = 7
    elif l == 2:
        values = counts.values()
        if 4 in values:
            rank = 6
        else:
            rank = 5
    elif l == 3:
        values = counts.values()
        c = Counter(values)

        if c[2] == 2:
            rank = 3
        else:
            rank = 4
        
    elif l == 4:
        rank = 2
    
    else:
        rank = 1

    if not dirty:
        return rank
    
    return StateGraph.get(rank).next(dirty)

    
def compare(arg1, arg2):
    arg1_ = arg1[0]
    arg2_ = arg2[0]

    type1 = type_checker(arg1_)
    type2 = type_checker(arg2_)

    points = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1, "J": 0}
    if type1 > type2:
        return 1
    
    elif type1 == type2:
        for c1, c2 in zip(arg1_, arg2_):
            if points.get(c1) > points.get(c2):
                return 1
            
            if points.get(c2) > points.get(c1):
                return -1
            
    else:
        return -1

with read_file() as handle:
    lines = handle.read().splitlines()
    hands = [
        (line.split(" ")[0], int(line.split(" ")[1]))
        for line in lines 
    ]
    
    total = 0
    for idx, (_, bet) in enumerate(sorted(hands, key=functools.cmp_to_key(compare))):
        total += bet * (idx + 1)

    print(total)


