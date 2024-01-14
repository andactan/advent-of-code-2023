import re

from mypackage_sina import read_file
from collections import defaultdict
from pprint import pprint


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

    queue = []
    for context_key in context.keys():
        queue.append((context_key, "in"))

    accepted = set()
    rejected = set()
    while queue:
        context_key, workflow_key = queue.pop(0)
        workflow = workflows[workflow_key]

        condition_ = False
        for condition, then in workflow.items():
            if eval(str(condition_)):
                continue

            if condition != "default":
                pattern = r'(?P<variable>[a-z]).+'
                m = re.search(pattern, condition).groupdict()

                condition_ = condition.replace(m["variable"], 
                                               context[context_key][m["variable"]])

            else:
                condition_ = True

            if eval(str(condition_)):
                if then == "A":
                    accepted.add(context_key)
                elif then == "R":
                    rejected.add(context_key)
                else:
                    queue.append((context_key, then))

    total = 0
    for context_key in accepted:
        variables = context[context_key]
        total += sum([int(item) for item in variables.values()])

    print(total)