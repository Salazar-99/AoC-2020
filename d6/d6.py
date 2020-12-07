INPUT_FILE = "input.txt"

with open(INPUT_FILE) as f:
    data = f.read()

chunks = data.split("\n\n")
#chunks = [chunk.replace("\n", "") for chunk in chunks]

def get_one_yes_qs(chunk: str) -> int:
    questions = set()
    for letter in chunk:
        questions.add(letter)
    return len(questions)

def get_all_yes_qs(chunk: str) -> int:
    lines = chunk.split("\n")
    sets = []
    for line in lines:
        questions = set()
        for letter in line:
            questions.add(letter)
        sets.append(questions)
    if len(sets) == 1:
        return len(sets[0])
    else:
        intersection = sets[0].intersection(sets[1])
        for i in range(2, len(sets)):
            intersection = intersection.intersection(sets[i])
        return len(intersection)
    

#print(sum([get_yes_qs(chunk) for chunk in chunks]))
print(sum([get_all_yes_qs(chunk) for chunk in chunks]))