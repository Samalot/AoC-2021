import Reader


def solve(line):
    tag_map = {'(': ')', '[': ']', '<': '>', '{': '}'}
    tag_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

    stack = []
    for char in line:
        if char in tag_map:
            stack.append(char)
        elif not char == tag_map[stack.pop()]:
            return tag_scores[char]
    return 0


def run():
    result = 0
    for data in Reader.read("input"):
        result += solve(data)
    return result


print(f'Answer: {run()}')
