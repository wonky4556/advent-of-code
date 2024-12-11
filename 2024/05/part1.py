with open("day5_input.txt", "r") as file:
    input = file.read()

(rules, updates) = input.split("\n\n")

rules = rules.split("\n")
updates = updates.split("\n")

rules = [[int(n) for n in r.split("|")] for r in rules]
updates = [[int(n) for n in u.split(",")] for u in updates]

def validate(rules, update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[1]) < update.index(rule[0]):
                return False
    return True    

result = 0

for update in updates:
    if validate(rules, update):
        result += update[len(update) // 2]

print(result)