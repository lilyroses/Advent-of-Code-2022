"""Tests for the Day 6 Solution"""

from solution import find_packet_stream_start


STREAM_1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
ANS_1_1 = 7
ANS_1_2 = 19

STREAM_2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
ANS_2_1 = 5
ANS_2_2 = 23

STREAM_3 = 'nppdvjthqldpwncqszvftbrmjlhg'
ANS_3_1 = 6
ANS_3_2 = 23

STREAM_4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
ANS_4_1 = 10
ANS_4_2 = 29

STREAM_5 ='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
ANS_5_1 = 11
ANS_5_2 = 26


def test_1():
    """Test 1"""
    assert find_packet_stream_start(STREAM_1) == ANS_1_1
    assert find_packet_stream_start(STREAM_1) == ANS_1_2

def test_2():
    """Test 2"""
    assert find_packet_stream_start(STREAM_2) == ANS_2_1
    assert find_packet_stream_start(STREAM_2) == ANS_2_2

def test_3():
    """Test 3"""
    assert find_packet_stream_start(STREAM_3) == ANS_3_1
    assert find_packet_stream_start(STREAM_3) == ANS_3_2

def test_4():
    """Test 4"""
    assert find_packet_stream_start(STREAM_4) == ANS_4_1
    assert find_packet_stream_start(STREAM_4) == ANS_4_2

def test_5():
    """Test 5"""
    assert find_packet_stream_start(STREAM_5) == ANS_5_1
    assert find_packet_stream_start(STREAM_5) == ANS_5_2


print(find_packet_stream_start(STREAM_1))
print(find_packet_stream_start(STREAM_2))
print(find_packet_stream_start(STREAM_3))
print(find_packet_stream_start(STREAM_4))
print(find_packet_stream_start(STREAM_5))