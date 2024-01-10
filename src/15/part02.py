from mypackage_sina import read_file
from collections import defaultdict

with read_file() as handle:
    codes = handle.readline().strip().split(',')
    
    boxes = defaultdict(dict)
    for code in codes:
        box_number = 0
        focal_length = None
        operation = 'boxes[{box_number}]'

        if '=' in code:
            focal_length = code[-1]
            code = code[:-2]
            operation += '.update({code}={focal_length})'

        if '-' in code:
            code = code[:-1]
            operation += '.pop("{code}", None)'

        for item in code:
            box_number += ord(item)
            box_number = (box_number * 17) % 256

        operation_formatted = operation.format(box_number=box_number, code=code, focal_length=focal_length)
        eval(operation_formatted)

    print(boxes)
    result = 0
    for box_number, lenses in (boxes.items()):
        for lens_number, (_, focal_length) in enumerate(lenses.items()):
            result += (box_number + 1) * (lens_number + 1) * focal_length

    print(result)