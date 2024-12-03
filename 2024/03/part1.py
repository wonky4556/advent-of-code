import re

with open("day3_input.txt", "r") as file:
    corruptedInput = ''.join([line.strip() for line in file])

val = sum(int(x) * int(y) for x, y in (seq.split(',') for seq in re.findall(r"mul\((\d{1,3},\d{1,3})\)", corruptedInput)))

print(val)