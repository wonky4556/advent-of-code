map = []

with open("day6_input.txt", "r") as file:
    map = [list(line.strip()) for line in file]

def traverse(map):
    moves, lookup = 0, {"V", "^", "<", ">"}
    current_index = next(((r, c) for r, row in enumerate(map) for c, val in enumerate(row) if val in lookup), (0, 0))

    while True:
        r, c = current_index
        if not (0 <= r < len(map)) or not (0 <= c < len(map[0])):
            break
        
        v = map[r][c]
        step = step_definition(v)
        nR, nC = r + step[0], c + step[1]

        if not (0 <= nR < len(map)) or not (0 <= nC < len(map[0])):
            moves += 1
            break

        nV = map[nR][nC]

        if nV in {".", "X"}:
            map[r][c], map[nR][nC] = "X", v
            current_index = (nR, nC)
            if nV == ".":
                moves += 1
        elif nV == "#":
            map[r][c] = replace(v)

    return moves
    
def replace(direction):
    return {"V": "<", "^": ">", "<": "^", ">": "V"}.get(direction, direction)

def step_definition(direction):
    return {"V": (1, 0), "^": (-1, 0), "<": (0, -1), ">": (0, 1)}.get(direction)

print(traverse(map))