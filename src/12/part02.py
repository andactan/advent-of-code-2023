import random

from mypackage_sina import read_file
from collections import defaultdict


class State:
    def __init__(self, dot_next, hash_next, terminate=False):
        self.dot_next = dot_next
        self.hash_next = hash_next
        self.checksum = random.getrandbits(64)
        self.terminate = terminate
    
    def __hash__(self) -> int:
        return self.checksum

with read_file() as handle:
    lines = handle.read().splitlines()
    total = 0
    for line in lines:
        springs, patterns = line.split(" ")
        patterns = [int(item) for item in patterns.split(',')]
        springs = '?'.join([springs] * 5)
        patterns = patterns * 5

        start = State(None, None)
        curr = start
        for pattern in patterns[:-1]:
            curr.dot_next = curr

            for _ in range(pattern):
                curr.hash_next = State(None, None)
                curr = curr.hash_next

            curr.dot_next = State(None, None)
            curr = curr.dot_next

        curr.dot_next = curr
        for _ in range(patterns[-1]):
            curr.hash_next = State(None, None)
            curr = curr.hash_next
        
        curr.terminate = True

        curr.dot_next = curr

        pointers = {start: 1}
        for spring in springs:

            temp_pointers = defaultdict(int)
            for pointer, value in pointers.items():
                temp1 = None
                temp2 = None
                if spring == '.':
                    temp1 = pointer.dot_next

                elif spring == '#':
                    temp1 = pointer.hash_next

                else:
                    temp1 = pointer.dot_next
                    temp2 = pointer.hash_next

                if temp1:
                    temp_pointers[temp1] += value
                
                if temp2:
                    temp_pointers[temp2] += value

            pointers = temp_pointers

        
        for pointer, value in pointers.items():
            if pointer.terminate:
                total += value

    print(total)