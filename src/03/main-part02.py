import os
import re


def solve():
    with open(os.path.join(os.getcwd(), 'day-03', 'input-part02.txt'), 'r') as handle:
        lines = handle.readlines()

        numbers = list() # store the numbers with position (i, j)
        specials = set() # store the position (i, j) and neighbor cells of special characters
        for i, line in enumerate(lines):
            m_numbers = re.finditer(r"[0-9]+", line)
            m_specials = re.finditer(r"[\*]", line)

            for m_number in m_numbers:
                numbers.append((m_number.group(0), i, m_number.start(0), m_number.end(0))) # end excluding

            for m_special in m_specials:
                specials.add((i, m_special.start(0)))
        
        result = 0
        found = dict()
        for number_t in numbers:
            num, i, start, end = number_t
            print(num)
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

                special_chars = specials.intersection(neighbors)
                if (special_chars):
                    for special_char in list(special_chars):
                        if special_char in found:
                            if len(found[special_char]) == 1:
                                result += int(num) * found[special_char][0]                                
                        else:
                            found[special_char] = [int(num)]

                    break
        
        print(result)
        return result

          
solve()