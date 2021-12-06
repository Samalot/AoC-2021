import Reader


def run():
    # Count the total amount of each fish at a given timer
    counts = [0] * 9

    # Read in seed data
    for data in Reader.read("input"):
        for fish in data.split(','):
            counts[int(fish)] += 1

    # Loop for 256 days
    for day in range(256):
        # Save the number of fish currently reproducing
        number_of_zeros = counts[0]

        # Shift all other fish down a cycle
        for i in range(1, len(counts)):
            counts[i-1] = counts[i]

        # Reset the 0 fish and add new batch of fish
        counts[8] = number_of_zeros
        counts[6] += number_of_zeros

    return sum(counts)


print(f'Answer: {run()}')
