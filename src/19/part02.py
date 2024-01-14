import re

from mypackage_sina import read_file
from collections import defaultdict
from pprint import pprint
from copy import deepcopy


with read_file() as handle:
    lines = handle.read().splitlines()

    workflows = defaultdict(dict)
    context, curr_context_id = dict(), 0
    for line in lines:
        if line.strip() == '':
            continue

        elif line.startswith("{"):
            pattern = r'{x=(?P<x>[0-9]+),m=(?P<m>[0-9]+),a=(?P<a>[0-9]+),s=(?P<s>[0-9]+)}'
            m = re.search(pattern, line).groupdict()
            context[curr_context_id] = m
            curr_context_id += 1

        else:
            pattern = r'(?P<queue_id>[a-z]+){(?P<condition_branch>[a-zA-Z0-9:,><=]+)}'
            m = re.search(pattern, line).groupdict()
            queue_id, condition_branch = m["queue_id"], m["condition_branch"]
            
            for condition_block in condition_branch.split(","):
                if ":" in condition_block:
                    condition, then = condition_block.split(":")
                    workflows[queue_id][condition] = then

                else:
                    workflows[queue_id]["default"] = condition_block

    # ignore the parts in the .txt file and
    # add a custom part with all values set to None
    context = {1: {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}}

    queue = [(deepcopy(context[1]), "in")]

    accepted = set()
    rejected = set()
    total = 0
    while queue:
        curr_variables, workflow_key = queue.pop(0)
        workflow = workflows[workflow_key]

        next_curr_variables = deepcopy(curr_variables)
        for condition, then in workflow.items():
            copy_curr_variables = deepcopy(next_curr_variables)

            if condition != "default":
                pattern = r'(?P<variable>[a-z])(?P<operator>[><])(?P<limit>-?[0-9]+)'
                m = re.search(pattern, condition).groupdict()
                
                variable = m["variable"]
                operator = m["operator"]
                limit = int(m["limit"])

                if operator == ">":
                    copy_curr_variables[variable][0] = limit + 1
                    next_curr_variables[variable][1] = limit
                else:
                    copy_curr_variables[variable][1] = limit - 1
                    next_curr_variables[variable][0] = limit 
            
            if then == "A":
                temp = 1
                for variable, limits in copy_curr_variables.items():
                    temp *= (limits[1] - limits[0] + 1)
                total += temp
            elif then == "R":
                continue
            else:
                queue.append((deepcopy(copy_curr_variables), then))

    # for context_key in accepted:
    #     variables = context[context_key]
    #     total += sum([int(item) for item in variables.values()])

    print(total)