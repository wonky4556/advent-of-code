#read input 
file = open("day1_input.txt", "r")
content = file.readlines()
file.close()

#parse input
set1 = []
set2 = []
for line in content:
    val = line.strip().split()
    set1.append(int(val[0]))
    set2.append(int(val[1]))

sum = 0
for val1 in set1:
    matches = [x for x in set2 if x == val1]
    sum = sum + (val1 * len(matches))

print(sum)
    