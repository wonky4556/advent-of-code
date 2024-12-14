import itertools

map = []

with open("day8_input.txt", "r") as file:
    map = [list(line) for line in file.read().split("\n")]

a_locations = {}

for r, row in enumerate(map):
    for c, col in enumerate(row):
        if col != ".":
            if col not in a_locations:
                a_locations[col] = []
            a_locations[col].append((r, c))

antinodes = set()
for frequency, locations in a_locations.items():
    for f_pair in itertools.combinations(locations, 2):
        (a, b) = f_pair
        dr = b[0] - a[0]
        dc = b[1] - a[1]

        r = a[0] - dr
        c = a[1] - dc
        while 0 <= r < len(map) and 0 <= c < len(map[0]):
            antinodes.add((r, c))
            r-=dr
            c-=dc
        
        r = b[0] + dr
        c = b[1] + dc
        while 0 <= r < len(map) and 0 <= c < len(map[0]):
            antinodes.add((r, c))
            r+=dr
            c+=dc
        
for frequency, locations in a_locations.items():
    if len(locations) > 1:
        antinodes.update(locations)

print(len(antinodes))

