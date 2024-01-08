from mypackage_sina import read_file
from scipy.spatial.distance import cdist

with read_file() as handle:
    lines = handle.read().splitlines()

    galaxy_arr = []
    rows_set = set()
    cols_set = set()
    for idx, line in enumerate(lines):
        temp = [[idx, i] for i, item in enumerate(line) if item == '#']
        galaxy_arr = [*galaxy_arr, *temp]
        
        if temp:
            rows_set.add(idx)
            cols_set.update([j for _, j in temp])

    rows_set = set(range(len(lines))).difference(rows_set)
    cols_set = set(range(len(lines[0]))).difference(cols_set)
    print(galaxy_arr)

    for idx, galaxy in enumerate(galaxy_arr):
        temp = [*galaxy]
        for row in rows_set:
            if galaxy[0] > row:
                temp[0] += 999_999
        galaxy_arr[idx] = temp

    for idx, galaxy in enumerate(galaxy_arr):
        temp = [*galaxy]
        for col in cols_set:
            if galaxy[1] > col:
                temp[1] += 999_999
        galaxy_arr[idx] = temp
        
    print(sum(sum(cdist(galaxy_arr, galaxy_arr, 'cityblock'))) / 2)