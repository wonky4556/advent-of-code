map = []

with open("day6_input.txt", "r") as file:
    map = [list(line.strip()) for line in file]

g_r = None
g_c  = None

for r, row in enumerate(map):
    for c, val in enumerate(row):
        if val == "^":
            g_r = r
            g_c = c
            break

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def traverse(map, g_r, g_c):
    d = 0
    path = set([(directions[d], g_r, g_c)])

    while True:
        nR = g_r + directions[d%4][0]
        nC = g_c + directions[d%4][1]
        
        if not (0 <= nR < len(map)) or not (0 <= nC < len(map[0])):
            return (False, path)

        blocked = map[nR][nC] == "#"

        if blocked:
            d += 1
        else:
            g_r = nR
            g_c = nC

        current = (directions[d%4], g_r, g_c)
        if current in path:
            return (True, path)
        else:
            path.add(current)

(_, path) = traverse(map, g_r, g_c)

sanitizedPath = set([(p[1], p[2]) for p in list(path)[1:]])

count = 0
for p in sanitizedPath:
    (r, c) = p
    map[r][c] = "#"
    if traverse(map, g_r, g_c)[0]:
        count+=1
    map[r][c] = "."

print(count)