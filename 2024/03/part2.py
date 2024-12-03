import re

def getSanitizedValue(corruptedInput):
    return sum(int(x) * int(y) for x, y in (seq.split(',') for seq in re.findall(r"mul\((\d{1,3},\d{1,3})\)", corruptedInput)))

with open("day3_input.txt", "r") as file:
    corruptedInput = ''.join(line.strip() for line in file)

finalVal = sum(getSanitizedValue(do.split("don't()")[0]) for do in re.split(r"do\(\)", corruptedInput))

print(finalVal)