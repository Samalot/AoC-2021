import Reader

def solve(training_data, input_data):
    solved_numbers, solved_segments = {}, {}

    # Identify numbers of unique lengths
    unique = {2: 1, 3: 7, 4: 4, 7: 8}
    size_bins = { 5: [], 6: [] }
    for data in training_data.split(" "):
        if len(data) in unique:
            solved_numbers[unique[len(data)]] = set([c for c in data])
        else:
            size_bins[len(data)].append(set([c for c in data]))

    # If subtract each 6 segment number from '8' and take the union
    # you get the set containing segments 'c, d, e'
    # subtract '4' from this, to find segment 'e'
    c_d_e = set.union(*[solved_numbers[8] - number for number in size_bins[6]])
    solved_segments['e'] = list(c_d_e - solved_numbers[4])[0]

    # Find the 5 segment number that has a difference of 1 to each of the other 5 segments
    # this is number '3'
    # Out of the two remaining 5 segment numbers, the one without 'e' is number 5
    if len(size_bins[5][0] - size_bins[5][1]) == 1:
        if len(size_bins[5][0] - size_bins[5][2]) == 1:
            solved_numbers[3] = size_bins[5][0]
            solved_numbers[5] = size_bins[5][1] if not solved_segments['e'] in size_bins[5][1] else size_bins[5][2]

        else:
            solved_numbers[3] = size_bins[5][1]
            solved_numbers[5] = size_bins[5][0] if not solved_segments['e'] in size_bins[5][0] else size_bins[5][2]
    else:
        solved_numbers[3] = size_bins[5][2]
        solved_numbers[5] = size_bins[5][0] if not solved_segments['e'] in size_bins[5][0] else size_bins[5][1]

    # Segment b is the remaining segment when you take 3 from 5
    solved_segments['b'] = list(solved_numbers[5] - solved_numbers[3])[0]

    # Segment d is the remaining segment when you take 1 from 4 and then remove segment b
    solved_segments['d'] = list(solved_numbers[4] - solved_numbers[1] - {solved_segments['b']})[0]

    # At this point we have solved numbers 1, 3, 4, 5, 7, 8
    # And have decoded segments 'b', 'd' and 'e'
    # Iterate over the input data to decode each number
    decoded_string = ''
    for number in input_data.split(" "):
        number_set = set([c for c in number])
        if len(number_set) in unique:
            decoded_string += str(unique[len(number_set)])
        elif len(number_set) == 5 and solved_segments['b'] in number_set:
            decoded_string += '5'
        elif len(number_set) == 5 and solved_segments['e'] in number_set:
            decoded_string += '2'
        elif len(number_set) == 6 and not solved_segments['d'] in number_set:
            decoded_string += '0'
        elif len(number_set) == 6 and solved_segments['e'] in number_set:
            decoded_string += '6'
        elif len(number_set) == 6:
            decoded_string += '9'
        else:
            decoded_string += '3'

    return int(decoded_string)


def run():
    total = 0
    for data in Reader.read("input"):
        training_data, input_data = data.split(" | ")
        total += solve(training_data, input_data)
    return total


print(f'Answer: {run()}')
