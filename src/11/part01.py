from mypackage_sina import read_file


with read_file() as handle:
    lines = handle.read().splitlines()

    galaxy_arr = []
    rows_set = set()
    cols_set = set()
    for idx, line in enumerate(lines):
        temp = [(idx, i) for i, item in enumerate(line) if item == '#']
        galaxy_arr = [*galaxy_arr, *temp]
        
        if temp:
            rows_set.add(idx)
            cols_set.update([j for _, j in temp])

    print(galaxy_arr)
    print(rows_set)
    print(cols_set)