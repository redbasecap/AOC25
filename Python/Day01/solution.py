#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 1: Secret Entrance
"""


def solve_day1_part1(input_file):
    """
    Simulate dial rotations and count how many times the dial points at 0
    after a rotation completes.
    """
    # Read the input
    with open(input_file, "r") as f:
        rotations = [line.strip() for line in f.readlines()]

    # Start at position 50
    position = 50
    count_at_zero = 0

    # Process each rotation
    for rotation in rotations:
        # Parse the rotation
        direction = rotation[0]  # 'L' or 'R'
        distance = int(rotation[1:])

        # Calculate new position
        if direction == "L":
            position = (position - distance) % 100
        else:  # direction == 'R'
            position = (position + distance) % 100

        # Check if dial is at 0
        if position == 0:
            count_at_zero += 1

    return count_at_zero


def solve_day1_part2(input_file):
    """
    Simulate dial rotations and count every time the dial passes through 0,
    including during rotations.
    """
    # Read the input
    with open(input_file, "r") as f:
        rotations = [line.strip() for line in f.readlines()]

    # Start at position 50
    position = 50
    count_at_zero = 0

    # Process each rotation
    for rotation in rotations:
        # Parse the rotation
        direction = rotation[0]  # 'L' or 'R'
        distance = int(rotation[1:])

        # Count how many times we pass through 0 during this rotation
        if direction == "L":
            # Moving left (toward lower numbers)
            for _ in range(distance):
                position = (position - 1) % 100
                if position == 0:
                    count_at_zero += 1
        else:  # direction == 'R'
            # Moving right (toward higher numbers)
            for _ in range(distance):
                position = (position + 1) % 100
                if position == 0:
                    count_at_zero += 1

    return count_at_zero


if __name__ == "__main__":
    input_file = "input.txt"
    answer_part1 = solve_day1_part1(input_file)
    answer_part2 = solve_day1_part2(input_file)
    print(f"Part 1 - The password is: {answer_part1}")
    print(f"Part 2 - The password is: {answer_part2}")
