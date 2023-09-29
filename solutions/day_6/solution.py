"""Solution for Day 6, Advent of Code 2022."""

INPUT_FILE = '/home/lilyroses/code/Advent-of-Code-2022/solutions/day_6/input.txt'

with open(INPUT_FILE, 'r') as f:
    STREAM = f.read()


# PART I

<<<<<<< HEAD
def find_packet_marker(stream, x):
    """Find the first chunk of four letters with no repeating letters."""

    # Using stream[i:j] gives us a chunk of letters at a time
    i = 0
    j = x
=======
def find_packet_stream_start(stream: str, chunk_size: int) -> int:
    """Find the first chunk of specified number of letters with no repeating letters."""
>>>>>>> 5691d079e5f41673689e76b6686bb841841d1d04
    
    # Setting j to initial value of chunk_size keeps chunk size the same when adding 1
    # to both i and j to check all of the stream's characters. 
    i = 0
    j = chunk_size # Saves chunk_size for all iterations
    
    # Once j equals one less than the number of characters in the stream, we have
    # reached the index of the final character in the stream. 
    while j < len(stream):
        # For chunk_size 4, chunk will be stream[0:4], stream[1:5], etc. 
        chunk = stream[i:j]

        # Save only unique letters in each chunk to this string. 
        uniques = ''
        # Iterate through the letters in the current chunk. 
        for letter in chunk:
            if letter not in uniques:
                uniques += letter

        # If the number of letters in uniques was not found. 
        if len(uniques) == chunk_size:
            # Return the final index of the stream where the chunk was found.
            return j

        # If the chunk was not found, add 1 to both j and i to iterate
        # through the whole stream.
        i += 1
        j += 1

    # Executes only if no unique chunk is found. 
    return False


if __name__ == '__main__':        
    print(find_packet_marker(STREAM, 4))
    print(find_packet_marker(STREAM, 14))
