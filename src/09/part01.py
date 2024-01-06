from mypackage_sina import read_file


with read_file() as handle:
    lines = handle.read().splitlines()
    readings = [[int(item) for item in line.split(" ")] for line in lines]

    total = 0
    for reading in readings:
        temp = reading
        unknown = 0
        while any(temp):
            unknown -= temp[-1]
            temp = [x2-x1 for (x1, x2) in zip(temp[:-1], temp[1:])]
        total += -unknown
    
    print(total)