"""Tests for the Day 6 Solution"""

import day_6
from day_6 import solution

CHUNK_1 = 4
CHUNK_2 = 14

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


def test_1_1():
    """Test 1, Part I"""
    assert find_packet_marker(STREAM_1, CHUNK_1) == ANS_1_1

def test_1_2():
    """Test 1, Part II"""
    assert find_packet_marker(STREAM_1, CHUNK_2) == ANS_1_2

def test_2_1():
    """Test 2, Part I"""
    assert find_packet_marker(STREAM_2, CHUNK_1) == ANS_2_1

def test_2_2():
    """Test 2, Part II"""
    assert find_packet_marker(STREAM_2, CHUNK_2) == ANS_2_2

def test_3_1():
    """Test 3, Part I"""
    assert find_packet_marker(STREAM_3, CHUNK_1) == ANS_3_1

def test_3_2():
    """Test 3, Part II"""
    assert find_packet_marker(STREAM_3, CHUNK_2) == ANS_3_2

def test_4_1():
    """Test 4, Part I"""
    assert find_packet_marker(STREAM_4, CHUNK_1) == ANS_4_1

def test_4_2():
    """Test 4, Part II"""
    assert find_packet_marker(STREAM_4, CHUNK_2) == ANS_4_2

def test_5_1():
    """Test 5, Part I"""
    assert find_packet_marker(STREAM_5, CHUNK_1) == ANS_5_1

def test_5_2():
    """Test 5, Part II"""
    assert find_packet_marker(STREAM_5, CHUNK_2) == ANS_5_2
