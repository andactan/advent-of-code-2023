import os
import re

def solve():
    with open(os.path.join(os.getcwd(), "day-04", 'input-part01.txt'), "r") as handle:
        # Card <number>: <list of winning numbers> | <list of what you get>
        total = 0
        while line := handle.readline().strip():
            pattern = r'^Card\s+(?P<card_number>[0-9]*):\s+(?P<winning>([0-9]+\s*){10})\s+\|\s+(?P<played>([0-9]+\s*){25})$'

            match = (re.match(pattern, line).groupdict())
            print(match.get("card_number"))
            winning_numbers = [int(item) for item in match.get("winning").split(" ") if item != " " and item != ""]
            played_numbers = [int(item) for item in match.get("played").split(" ") if item != " " and item != ""]
            
            overlaps = set(winning_numbers).intersection(set(played_numbers))
            points = 2 ** (len(overlaps) - 1) if len(overlaps) > 0 else 0
            print(len(overlaps), points)  

            total += points
        print(total)


solve()
