import Reader


def processData():
    numbers, boards, newBoard = [], [], []
    for data in Reader.read("input"):
        if len(numbers) == 0:
            numbers = data.split(",")
        else:
            if not data == "":
                newBoard.append(list(filter(None, data.split(" "))))
            elif len(newBoard) == 5:
                boards.append(newBoard)
                newBoard = []
    boards.append(newBoard)
    return numbers, boards


def score(board, number):
    score = 0
    for rowScore in range(len(board)):
        for colScore in range(len(board[0])):
            if not board[rowScore][colScore] == "*":
                score += int(board[rowScore][colScore])
    return score * int(number)


def run():
    numbers, boards = processData()
    for number in numbers:
        for b in range(len(boards)):
            for row in range(len(boards[b])):
                for col in range(len(boards[b][0])):
                    if boards[b][row][col] == number:
                        boards[b][row][col] = "*"
                        completeRow = all([boards[b][row][x] == "*" for x in range(len(boards[b][row]))])
                        completeCol = all([boards[b][y][col] == "*" for y in range(len(boards[b]))])
                        if completeRow or completeCol:
                            return score(boards[b], number)
    return 0


print(f'Answer: {run()}')
