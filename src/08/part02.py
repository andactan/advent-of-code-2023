import re

from mypackage_sina import read_file
from math import lcm


with read_file() as handle:
    lines = handle.read().splitlines()
    instructions = list(lines[0])
    len_instructions = len(instructions)
    # skip the 2nd entry since it is an empty string
    map_ = dict()
    for line in lines[2:]:
        pattern = r'(?P<source>[0-9A-Z]+) = [(](?P<L>[0-9A-Z]+), (?P<R>[0-9A-Z]+)[)]'
        m = re.search(pattern, line).groupdict()
        map_.setdefault(m.get('source'), {'L': m.get('L'), 'R': m.get("R")})

    curr_points = [item for item in map_.keys() if item.endswith("A")]
    curr_instruction_idx = 0
    done = lambda x: all([item.endswith("Z") for item in x])

    num_steps_arr = []

    for curr_point in curr_points:
        temp = curr_point
        num_steps = 0
    
        while not done([temp]):
            curr_instruction = instructions[curr_instruction_idx]
            curr_instruction_idx = (curr_instruction_idx + 1) % len_instructions
            temp = map_.get(temp).get(curr_instruction)
            num_steps += 1

        num_steps_arr.append(num_steps)

    print(lcm(*num_steps_arr))


