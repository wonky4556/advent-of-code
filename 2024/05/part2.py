with open("day5_input.txt", "r") as file:
    input = file.read()

(rules, updates) = input.split("\n\n")

rules = rules.split("\n")
updates = updates.split("\n")

rules = [[int(n) for n in r.split("|")] for r in rules]
updates = [[int(n) for n in u.split(",")] for u in updates]

# def validate(rules, update):
#     for rule in rules:
#         if rule[0] in update and rule[1] in update:
#             if update.index(rule[1]) < update.index(rule[0]):
#                 return False
#     return True

def fix(rules, update):
    numChanges = 0
    changed = True
    i = 0
    while changed:
        if i > len(update) - 1:
            break

        changed = False
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                a = update.index(rule[0])
                b = update.index(rule[1])

                if b < a:
                    changed = True
                    numChanges += 1
                    tmp = update[b]
                    update[b] = update[a]
                    update[a] = tmp

        i += 1

    return numChanges > 0

result = 0

for update in updates:
    if fix(rules, update):
        result += update[len(update) // 2]

print(result)