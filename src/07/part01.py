import functools

from mypackage_sina import read_file
from collections import Counter


def type_checker(arg):
    counts = Counter(arg)
    l = len(counts)

    if l == 1:
        return 7
    elif l == 2:
        values = counts.values()
        if 4 in values:
            return 6
        else:
            return 5
    elif l == 3:
        values = counts.values()
        c = Counter(values)

        if c[2] == 2:
            return 3
        else:
            return 4
        
    elif l == 4:
        return 2
    
    else:
        return 1
    
def compare(arg1, arg2):
    arg1_ = arg1[0]
    arg2_ = arg2[0]

    type1 = type_checker(arg1_)
    type2 = type_checker(arg2_)

    points = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
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

    # print(type_checker("QQQJA"))

    total = 0
    for idx, (_, bet) in enumerate(sorted(hands, key=functools.cmp_to_key(compare))):
        total += bet * (idx + 1)

    print(total)

