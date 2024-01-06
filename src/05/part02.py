from mypackage_sina import read_file


with read_file() as handle:
    keys = list(reversed([
        "seed-to-soil map:",
        "soil-to-fertilizer map:",
        "fertilizer-to-water map:",
        "water-to-light map:",
        "light-to-temperature map:",
        "temperature-to-humidity map:",
        "humidity-to-location map:"
    ]))

    lines = handle.read().splitlines()

    # first line always contains seed numbers
    seed_numbers = [int(item) for item in lines[0].split('seeds: ')[1].split(" ")]
    maps = dict()
    curr_key = keys.pop()
    old_key = curr_key
    for line in [item for item in lines[1:] if item != ""]:
        if curr_key == line:
            maps[curr_key] = []

            old_key = curr_key
            curr_key = keys.pop() if keys else None
        else:
            maps[old_key].append(line)


    for key, values in maps.items():
        queue = seed_numbers
        seed_numbers = []

        while queue:
            seed_number_start = queue.pop(0)
            seed_number_range = queue.pop(0)
            seed_range = [seed_number_start, seed_number_start + seed_number_range - 1]
            changed = False
            for value in values:
                # destination, source, period
                # find overlapping numbers between [source, source+range> and [seed, seed+seed_range>
                dest, source, map_range = [int(item) for item in value.split(" ")]
                source_range = [source, source + map_range - 1]

                if seed_range[1] < source_range[0]:
                    # no overlap
                    continue

                if source_range[1] < seed_range[0]:
                    # no overlap
                    continue

                start = source_range[0] if seed_range[0] < source_range[0] else seed_range[0]
                end = source_range[1] if seed_range[1] > source_range[1] else seed_range[1]

                left = []
                right = []
                if start > seed_range[0]:
                    left = [seed_range[0], start - seed_range[0]]

                if end < seed_range[1]:
                    right = [end + 1, seed_range[1] - end]

                converted_start = start - source + dest
                converted = [converted_start, end - start + 1]

                seed_numbers = [*seed_numbers, *converted]
                queue = [*queue, *left, *right]
                changed = True

                break
            
            if not changed:
                seed_numbers = [*seed_numbers, seed_number_start, seed_number_range]

        print(key, seed_numbers)

    print(min(seed_numbers[::2])) 
            

    
