import itertools

values = []
calibrators = []

with open("day7_input.txt", "r") as file:
    for line in file:
        values.append(int(line.split(":")[0]))
        val = line.split(":")[1]
        vals = [int(v) for v in val.split()]
        calibrators.append(vals)    

operations = [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(str(x) + str(y))]

def evaluate(calibrator, ops):
    n = calibrator.copy()
    n.reverse()
    r = n.pop()
    ops.reverse()
    while len(n):
        o = ops.pop()
        r = operations[o](r, n.pop())

    return r

sum = 0

for i, calibrator in enumerate(calibrators):
    ops = list(itertools.product(range(len(operations)), repeat=len(calibrator)-1))
    for o in ops:
        if evaluate(calibrator, list(o)) == values[i]:
            sum += values[i]
            break

print(sum)

    