#read input 
file = open("day2_input.txt", "r")
content = file.readlines()
file.close()

reports = []
for line in content:
    reports.append([int(n) for n in line.strip().split()])

def isDirectional(report):
    is_ascending = [(report[i] < report[i + 1] for i in range(len(report) - 1))]
    is_descending = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    return is_ascending or is_descending

def isWithinTolerance(report):
    diffs = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]
    return all([diff >= 1 and diff <= 3 for diff in diffs])

count = 0
for report in reports:
    if isDirectional(report) and isWithinTolerance(report):
        count = count + 1

print(count)