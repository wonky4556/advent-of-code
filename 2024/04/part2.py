matrix = []

with open("day4_input.txt", "r") as file:
    matrix = [list(line.strip()) for line in file]

SEARCH_WORD = "XMAS"
        
def searchGrid(grid, r, c):
    return any(
        [
            # M S
            #  A
            # M S
            all([
                grid[r - 1][c - 1] == "M",
                grid[r - 1][c + 1] == "S",
                grid[r + 1][c - 1] == "M",
                grid[r + 1][c + 1] == "S"
            ]),
            # S S
            #  A
            # M M
            all([
                grid[r - 1][c - 1] == "S",
                grid[r - 1][c + 1] == "S",
                grid[r + 1][c - 1] == "M",
                grid[r + 1][c + 1] == "M"
            ]),
            # S M
            #  A
            # S M
            all([
                grid[r - 1][c - 1] == "S",
                grid[r - 1][c + 1] == "M",
                grid[r + 1][c - 1] == "S",
                grid[r + 1][c + 1] == "M"
            ]),
            # M M
            #  A
            # S S
            all([
                grid[r - 1][c - 1] == "M",
                grid[r - 1][c + 1] == "M",
                grid[r + 1][c - 1] == "S",
                grid[r + 1][c + 1] == "S"
            ]),
        ]
    )


count = 0
for r in range(1, len(matrix) - 1):
    for c in range(1, len(matrix[0]) - 1):
        if matrix[r][c] != "A":
            continue
        if searchGrid(matrix, r, c):
            count += 1

print(count)
        