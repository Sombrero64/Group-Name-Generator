from random import randint

adjectives, nouns, plural = [
    "Annoying",
    "Angry",
    "Brave",
    "Wired",
    "Silly",
    "Inner",
    "Outer",
    "Inway",
    "Outway",
    "Peaceful",
    "Nice",
    "Happy",
    "Sad"
], [
    "Apple",
    "Bear",
    "Brain",
    "Bird",
    "Cat",
    "Computer",
    "Pie",
    "Dog",
    "Sloth",
    "Processor",
    "Robot",
    "Human"
], True

used = []
def randt(table): return table[randint(0, len(table) - 1)]
def contains(table, item):
    for i in table:
        if i == item: return True
    return False

def generateName():
    while True:
        # generate new name
        name = str(randt(adjectives)) + str(randt(nouns))
        if plural: name += 's'

        # add name
        if not contains(used, name):
            used.append(name)
            break

for a in range(1, 10, 1): generateName()
for b in used: print(b)
