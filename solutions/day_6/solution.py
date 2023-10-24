"""Solution for Day 6, Advent of Code 2022."""

INPUT_FILE = '/home/lilyroses/code/Advent-of-Code-2022/solutions/day_6/input.txt'

with open(INPUT_FILE, 'r', encoding="utf-8") as f:
    lines = f.read()


# PART I

def find_packet_stream_start(text_stream: str, chunk_size: int) -> int:
    """Find the first chunk of specified number of letters with no repeating letters."""

    # Setting j to initial value of chunk_size keeps chunk size the same when adding 1
    # to both i and j to check all of the text stream's characters.
    i = 0
    j = chunk_size # Saves chunk_size for all iterations

    # Once j equals one less than the number of characters in the text stream, we have
    # reached the index of the final character in the text stream.
    while j < len(text_stream):
        # For chunk_size 4, chunk will be text stream[0:4], text stream[1:5], etc.
        chunk = text_stream[i:j]

        # Save only unique letters in each chunk to this string.
        uniques = ''
        # Iterate through the letters in the current chunk.
        for letter in chunk:
            if letter not in uniques:
                uniques += letter

        # If the number of letters in uniques was not found.
        if len(uniques) == chunk_size:
            # Return the final index of the text stream where the chunk was found.
            return j

        # If the chunk was not found, add 1 to both j and i to iterate
        # through the whole stream.
        i += 1
        j += 1

    # Executes only if no unique chunk is found.
    return False


if __name__ == '__main__':
    print(find_packet_stream_start(lines, 4))
    print(find_packet_stream_start(lines, 14))
