import Reader


def run():
    total = 0
    for data in Reader.read("input"):
        for segments in data.split(" | ")[1].split(" "):
            if not (len(segments) == 5 or len(segments) == 6):
                total += 1

    return total


print(f'Answer: {run()}')
