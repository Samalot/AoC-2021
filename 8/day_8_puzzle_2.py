import Reader


def solve(training_data, input_data):
    solved_numbers, solved_segments = {}, {}
    unique = {2: 1, 3: 7, 4: 4, 7: 8}
    size_bins = { 5: [], 6: [] }

    for data in training_data.split(" "):
        data_set = set([c for c in data])
        if len(data) in unique:
            solved_numbers[unique[len(data)]] = data_set
        else:
            size_bins[len(data)].append(data_set)

    c_d_e = set.union(*[solved_numbers[8] - number for number in size_bins[6]])
    solved_segments['e'] = list(c_d_e - solved_numbers[4])[0]

    if len(size_bins[5][0] - size_bins[5][1]) == 1:
        if len(size_bins[5][0] - size_bins[5][2]) == 1:
            solved_numbers[3] = size_bins[5][0]
            solved_numbers[5] = size_bins[5][1] if not solved_segments['e'] in size_bins[5][1] else size_bins[5][2]
        else:
            solved_numbers[3] = size_bins[5][1]
            solved_numbers[5] = size_bins[5][0]if not solved_segments['e'] in size_bins[5][0] else size_bins[5][2]
    else:
        solved_numbers[3] = size_bins[5][2]
        solved_numbers[5] = size_bins[5][0] if not solved_segments['e'] in size_bins[5][0] else size_bins[5][1]

    for number in size_bins[6]:
        if solved_numbers[8] - number == {solved_segments['e']}:
            solved_numbers[9] = number
        elif solved_numbers[8] - number == solved_numbers[3] - solved_numbers[5]:
            solved_numbers[6] = number

    mapped_numbers = {}
    for key in solved_numbers:
        mapped_numbers[str(sorted(solved_numbers[key]))] = str(key)

    decoded_string = ''
    for number in input_data.split(" "):
        number_set = set([c for c in number])
        if len(number_set) in unique:
            decoded_string += str(unique[len(number_set)])
        elif str(sorted(number_set)) in mapped_numbers:
            decoded_string += mapped_numbers[str(sorted(number_set))]
        elif len(number_set) == 5:
            decoded_string += '2'
        else:
            decoded_string += '0'

    return int(decoded_string)


def run():
    total = 0
    for data in Reader.read("input"):
        training_data, input_data = data.split(" | ")
        total += solve(training_data, input_data)

    return total


print(f'Answer: {run()}')
