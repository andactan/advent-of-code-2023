from mypackage_sina import read_file


with read_file() as handle:
    lines = handle.read().splitlines()
    num_rows = len(lines)
    num_cols = len(lines[0])

    queue = [(0, 0, "e")]
    visited = []
    while queue:
        x, y, direction = queue.pop(0)

        if tuple((x, y, direction)) in visited:
            continue

        if x < 0 or x >= num_rows:
            continue

        if y < 0 or y >= num_cols:
            continue
        
        visited.append((x, y, direction))
        tile = lines[x][y]
        
        if tile == "|":
            if direction in ["e", "w"]:
                queue.append((x - 1, y, "n")) 
                queue.append((x + 1, y, "s"))

            elif direction == "s":
                queue.append((x + 1, y, "s"))

            else:
                queue.append((x - 1, y, "n"))

        elif tile == "-":
            if direction in ["n", "s"]:
                queue.append((x, y + 1, "e"))
                queue.append((x, y - 1, "w"))

            elif direction == "e":
                queue.append((x, y + 1, "e"))

            else:
                queue.append((x, y - 1, "w"))

        elif tile == '/':
            if direction == "s":
                queue.append((x, y - 1, "w"))

            elif direction == "n":
                queue.append((x, y + 1, "e"))

            elif direction == "e":
                queue.append((x - 1, y, "n"))

            else:
                queue.append((x + 1, y, "s"))

        elif tile == "\\":
            if direction == "s":
                queue.append((x, y + 1, "e"))

            elif direction == "n":
                queue.append((x, y - 1, "w"))

            elif direction == "e":
                queue.append((x + 1, y, "s"))

            else:
                queue.append((x - 1, y, "n"))

        else:
            if direction == "e":
                queue.append((x, y + 1, "e"))

            elif direction == "w":
                queue.append((x, y - 1, "w"))

            elif direction == "n":
                queue.append((x - 1, y, "n"))

            else:
                queue.append((x + 1, y, "s"))

    print(len(set([(x, y) for x, y, d in visited])))





