import re
from typing import Any

from mypackage_sina import read_file
from collections import defaultdict


with read_file() as handle:
    lines = handle.read().splitlines()

    graph = defaultdict(lambda: {
        'fanin': [], 
        'fanout': [], 
        'next_state': False, 
        'state': False, 
        't': None
        }
    )
    
    for line in lines:
        pattern = r'^(?P<module_type>[%&])?(?P<module_start>[a-zA-Z]+) -> (?P<module_end>[a-zA-Z]+(, [a-zA-Z]+)*)$'
        m = re.search(pattern, line)

        module_type = m["module_type"]
        module_start = m["module_start"]
        module_end = m["module_end"].split(", ")

        if module_type is None:
            graph[module_start]["t"] = "broadcast"
            graph[module_start]["fanout"] = module_end
        
        elif module_type == "%":
            graph[module_start]["t"] = "flip-flop"  
            graph[module_start]["fanout"] = module_end

        else:
            graph[module_start]["t"] = "conjunction"
            graph[module_start]["fanout"] = module_end
            graph[module_start]["state"] = True

        for module in module_end:
            graph[module]["fanin"].append(module_start)
    
    high = 0
    low = 0
    for i in range(1000):
        low += 1 # button press
        queue = [("broadcaster", False)]
        visited = set()
        while queue:
            curr = queue.pop(0)
            
            module, pulse = curr
            graph[module]["state"] = graph[module]["next_state"]

            for next_module in graph[module]["fanout"]:
                if graph[next_module]["t"] == "flip-flop":
                    if not pulse:
                        graph[next_module]["next_state"] = not (pulse ^ graph[next_module]["state"])
                        queue.append((next_module, graph[next_module]["next_state"]))

                elif graph[next_module]["t"] == "conjunction":
                    temp = []
                    for conjunction_fanin in graph[next_module]["fanin"]:
                        temp.append(graph[conjunction_fanin]["state"])

                    graph[next_module]["next_state"] = not all(temp)
                    queue.append((next_module, graph[next_module]["next_state"]))

                # print(f"{module} - {pulse} - {next_module}")
                if pulse:
                    high += 1
                else:
                    low += 1

    print(high * low, high, low)
    
                
