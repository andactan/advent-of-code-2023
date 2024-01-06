import os
import re

def solve():
    with open(os.path.join(os.getcwd(), 'day-03', 'input-part01.txt'), 'r') as handle:
        lines = handle.readlines()

        numbers = list() # store the numbers with position (i, j)
        specials = set() # store the position (i, j) and neighbor cells of special characters
        for i, line in enumerate(lines):
            m_numbers = re.finditer(r"[0-9]+", line)
            m_specials = re.finditer(r"[^0-9\.\n]", line)

            for m_number in m_numbers:
                print(m_number.group(0))
                numbers.append((m_number.group(0), i, m_number.start(0), m_number.end(0))) # end excluding

            for m_special in m_specials:
                print(m_special)
                specials.add((i, m_special.start(0)))
        
        result = 0
        print(list(specials))
        for number_t in numbers:
            num, i, start, end = number_t
            for j in range(start, end):
                neighbors = set([
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1),
                    (i + 1, j + 1),
                    (i + 1, j - 1),
                    (i - 1, j + 1),
                    (i - 1, j - 1)
                ])

                found = specials.intersection(neighbors)

                if (found):
                    result += int(num)
                    break

        return result

          
solve()