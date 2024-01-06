import re

from mypackage_sina import read_file


with read_file() as handle:
    lines = handle.read().splitlines()
    instructions = list(lines[0])
    len_instructions = len(instructions)
    # skip the 2nd entry since it is an empty string
    map_ = dict()
    for line in lines[2:]:
        pattern = r'(?P<source>[A-Z]+) = [(](?P<L>[A-Z]+), (?P<R>[A-Z]+)[)]'
        m = re.search(pattern, line).groupdict()
        map_.setdefault(m.get('source'), {'L': m.get('L'), 'R': m.get("R")})

    curr_point = 'AAA'
    curr_instruction_idx = 0
    num_steps = 0
    while not curr_point == 'ZZZ':
        curr_instruction = instructions[curr_instruction_idx]
        curr_instruction_idx = (curr_instruction_idx + 1) % len_instructions
        curr_point = map_.get(curr_point).get(curr_instruction)
        num_steps += 1

    print(num_steps)


