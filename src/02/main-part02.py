import os
import re


def solve():
    # 12R, 13G, 14B
    with open(os.path.join(os.getcwd(), "day-02", 'input-part1.txt'), 'r') as handle:
        retval = 0
        while line := handle.readline().strip():
            [game_id, game_content] = line.split(':')
            
            turns = game_content.split(';')
            d = {"red": -1, "green": -1, "blue": -1}
            for turn in turns:
                pattern = r'((?P<red>[0-9]*) red|(?P<blue>[0-9]*) blue|(?P<green>[0-9]*) green)'
                matches = re.finditer(pattern, turn)
                
                for idx, match in enumerate(matches, start=1):
                    group_dict = {k: v for k, v in match.groupdict().items() if v is not None}
                    for key, value in match.groupdict().items():
                        if value is not None:
                            d[key] = max(d[key], int(value))

            
            retval += d["red"] * d["blue"] * d["green"]
        
        return retval

if __name__ == "__main__":
    print(solve())