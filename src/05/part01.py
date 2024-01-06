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
        print(curr_key, line)

        if curr_key == line:
            maps[curr_key] = []

            old_key = curr_key
            curr_key = keys.pop() if keys else None
        else:
            maps[old_key].append(line)


    print(seed_numbers)

    for key, values in maps.items():
        for idx, seed_number in enumerate(seed_numbers):
            # changed = False
            for value in values:
                # destination, source, period
                dest, source, period = [int(item) for item in value.split(" ")]

                if source <= seed_number < source + period:
                    seed_numbers[idx] = seed_number - source + dest
                    break

        print(key, seed_numbers)


    print(min(seed_numbers)) 
            

    
