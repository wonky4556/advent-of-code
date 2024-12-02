#read input 
file = open("day1-input.txt", "r")
content = file.readlines()
file.close()

#parse input
set1 = []
set2 = []
for line in content:
    val = line.strip().split()
    set1.append(int(val[0]))
    set2.append(int(val[1]))

#sort groups
set1.sort()
set2.sort()

#calculate differences and sum
sum = 0
for n in range(len(set1)):
    sum = sum + (abs(set1[n] - set2[n]))

print(sum)