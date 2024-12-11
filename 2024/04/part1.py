matrix = []

with open("day4_input.txt", "r") as file:
    matrix = [list(line.strip()) for line in file]

SEARCH_WORD = "XMAS"
        
def searchGrid(grid, r, c):
    steps = [
        (0,1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]

    count = 0

    for step in steps:
        word = []
        for i in range(len(SEARCH_WORD)):
            R = r + i * step[0]
            C = c + i * step[1]

            if R < 0:
                break
            if R > len(grid) - 1:
                break
            if C < 0:
                break
            if C > len(grid[0]) - 1:
                break
            word.append(grid[R][C])
        
        if word == ["X", "M", "A", "S"]:
            count += 1
    return count


count = 0
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] != "X":
            continue
        count += searchGrid(matrix, r, c)

print(count)
        