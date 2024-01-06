import os
import re

def solve():
    with open(os.path.join(os.getcwd(), "day-04", 'input-part02.txt'), "r") as handle:
        # Card <number>: <list of winning numbers> | <list of what you get>
        cards = {}
        while line := handle.readline().strip():
            pattern = r'^Card\s+(?P<card_number>[0-9]*):\s+(?P<winning>([0-9]+\s*){10})\s+\|\s+(?P<played>([0-9]+\s*){25})$'

            match = (re.match(pattern, line).groupdict())
            winning_numbers = [int(item) for item in match.get("winning").split(" ") if item != " " and item != ""]
            played_numbers = [int(item) for item in match.get("played").split(" ") if item != " " and item != ""]
            
            card_number = int(match.get("card_number"))
            next_cards = set(winning_numbers).intersection(set(played_numbers))

            if card_number not in cards:
                cards[card_number] = 1
            else:
                cards[card_number] += 1

            print(len(next_cards))
            for i in range(1, len(next_cards) + 1):
                if i + card_number not in cards:
                    cards[i + card_number] = cards[card_number]
                else:
                    cards[i + card_number] += cards[card_number]

            print(cards)

        total = 0
        for value in cards.values():
            total += value

        print(total)

solve()
