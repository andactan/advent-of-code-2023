from mypackage_sina import read_file
from collections import defaultdict

with read_file() as handle:
    codes = handle.readline().strip().split(',')
    
    result = 0
    boxes = defaultdict(dict)
    for code in codes:
        curr_val = 0
        for item in code:
            curr_val += ord(item)
            curr_val = (curr_val * 17) % 256

        result += curr_val


    print(result)