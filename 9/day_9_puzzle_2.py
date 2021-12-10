import Reader


def solve(line):
    tag_map = {'(': ')', '[': ']', '<': '>', '{': '}'}
    stack = []
    for char in line:
        if char in tag_map:
            stack.append(char)
        elif not char == tag_map[stack.pop()]:
            return 0

    tag_scores = {')': 1, ']': 2, '}': 3, '>': 4}
    total = 0
    for i in range(len(stack)):
        total = (total * 5) + tag_scores[tag_map[stack.pop()]]
    return total


def run():
    scores = []
    for data in Reader.read("input"):
        score = solve(data)
        if score > 0:
            scores.append(solve(data))
    return sorted(scores)[len(scores) // 2]


print(f'Answer: {run()}')
