#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 2: Gift Shop
Find invalid product IDs that are made of a sequence of digits repeated twice.
"""


def is_invalid_id_part1(num):
    """
    Check if a number is an invalid ID (Part 1).
    Invalid IDs are made of a sequence of digits repeated exactly twice.
    Examples: 55 (5 twice), 6464 (64 twice), 123123 (123 twice)
    """
    s = str(num)
    
    # Number must have even length to be a repeated pattern
    if len(s) % 2 != 0:
        return False
    
    # Check if first half equals second half
    mid = len(s) // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    return first_half == second_half


def is_invalid_id_part2(num):
    """
    Check if a number is an invalid ID (Part 2).
    Invalid IDs are made of a sequence of digits repeated at least twice.
    Examples: 11 (1 twice), 111 (1 thrice), 123123 (123 twice), 123123123 (123 thrice)
    """
    s = str(num)
    
    # Try all possible pattern lengths
    for pattern_len in range(1, len(s) // 2 + 1):
        pattern = s[:pattern_len]
        
        # Check if the number is made by repeating this pattern
        expected_repetitions = len(s) // pattern_len
        
        # Only valid if pattern length divides the string length evenly
        if len(s) % pattern_len != 0:
            continue
        
        # Check if repeating pattern creates the number
        if pattern * expected_repetitions == s and expected_repetitions >= 2:
            return True
    
    return False


def solve_part1(input_file):
    """
    Find all invalid IDs in the given ranges (Part 1) and sum them up.
    """
    with open(input_file, 'r') as f:
        content = f.read().strip()
    
    # Parse ranges
    ranges = content.split(',')
    
    total = 0
    
    for range_str in ranges:
        start, end = map(int, range_str.split('-'))
        
        # Check each number in the range
        for num in range(start, end + 1):
            if is_invalid_id_part1(num):
                total += num
    
    return total


def solve_part2(input_file):
    """
    Find all invalid IDs in the given ranges (Part 2) and sum them up.
    """
    with open(input_file, 'r') as f:
        content = f.read().strip()
    
    # Parse ranges
    ranges = content.split(',')
    
    total = 0
    
    for range_str in ranges:
        start, end = map(int, range_str.split('-'))
        
        # Check each number in the range
        for num in range(start, end + 1):
            if is_invalid_id_part2(num):
                total += num
    
    return total


if __name__ == "__main__":
    input_file = "input.txt"
    answer_part1 = solve_part1(input_file)
    answer_part2 = solve_part2(input_file)
    
    print(f"Part 1 - The answer is: {answer_part1}")
    print(f"Part 2 - The answer is: {answer_part2}")
