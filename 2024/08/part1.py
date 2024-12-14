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
        antinodes.add((a[0] - dr, a[1] - dc))
        antinodes.add((b[0] + dr, b[1] + dc))

valid = [
    n for n in antinodes if 0<=n[0]<len(map) and 0<=n[1]<len(map[0])
]

print(len(valid))