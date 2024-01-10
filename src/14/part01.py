from mypackage_sina import read_file


with read_file() as handle:
    lines = handle.read().splitlines()

    # store northmost point a rock can roll to while
    # analyzing (that's what she said) each row
    boundary = [-1 for _ in range(len(lines[0]))]
    rounded_rocks = []
    num_rows = len(lines)
    for i, line in enumerate(lines):
        for j, char_ in enumerate(line):
            if char_ == "#":
                boundary[j] = i

            elif char_ == "O":
                rounded_rocks.append(num_rows - (boundary[j] + 1))
                boundary[j] += 1

    print(sum(rounded_rocks))
