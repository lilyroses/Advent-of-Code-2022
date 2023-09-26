"""Solution for Day 6, Advent of Code 2022."""

INPUT_FILE = '/home/lilyroses/code/Advent-of-Code-2022/solutions/day_6/input.txt'

with open(INPUT_FILE, 'r') as f:
    STREAM = f.read()


# PART I

def find_packet_stream_start(stream):
    """Find the first chunk of four letters with no repeating letters."""

    # Using stream[i:j] gives us a chunk of four letters at a time
    j = 4
    i = 0

    # Once j is one less than the length of the stream, we have
    # reached the final character in the stream's index
    while j < len(stream):
        chunk = stream[i:j]

        # Save unique letters in each four letter chunk to this string
        uniques = ''
        # Iterate through the letters in the four letter chunk
        for letter in chunk:
            if letter not in uniques:
                uniques += letter

        # Letters are only saved to uniques if they are unique,
        # so if uniques does not have four letters, there was a
        # repeating letter
        if len(uniques) == 4:
            # return final index of the stream where chunk was found
            return j

        # If the chunk was not found, add 1 to both j and i to iterate
        # through the whole stream
        i += 1
        j += 1

    # If no unique chunk found
    return -1


if __name__ == '__main__':        
    print(find_packet_stream_start(STREAM))
