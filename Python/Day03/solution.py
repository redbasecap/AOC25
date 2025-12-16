#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 3: Lobby
Find maximum joltage by selecting two batteries from each bank.
"""


def solve_part1(input_file):
    """
    For each bank (line), find the pair of digits at positions i < j that forms
    the maximum joltage. You cannot rearrange batteries.
    Sum all the maximum joltages.
    """
    with open(input_file, "r") as f:
        lines = f.read().strip().split("\n")

    total_joltage = 0

    for line in lines:
        if not line:
            continue

        # Try all pairs of positions (i, j) where i < j
        max_joltage = 0
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                # Form the joltage from digits at positions i and j (in order)
                joltage = int(line[i] + line[j])
                max_joltage = max(max_joltage, joltage)

        total_joltage += max_joltage

    return total_joltage


def solve_part2(input_file):
    """
    For each bank (line), find the largest 12-digit joltage by selecting
    12 batteries while maintaining their order.
    Use a greedy algorithm: for each position, pick the largest digit
    that still leaves enough digits to complete the selection.
    """
    with open(input_file, "r") as f:
        lines = f.read().strip().split("\n")

    total_joltage = 0
    target_length = 12

    for line in lines:
        if not line:
            continue

        # Greedy approach: for each position in result, find the largest digit
        result = []
        start_idx = 0
        remaining_to_pick = target_length

        for _ in range(target_length):
            # How many digits can we skip?
            available = len(line) - start_idx
            can_skip = available - remaining_to_pick

            # Find the maximum digit in the range we can pick from
            max_digit = None
            max_idx = -1
            for idx in range(start_idx, start_idx + can_skip + 1):
                if max_digit is None or line[idx] > max_digit:
                    max_digit = line[idx]
                    max_idx = idx

            result.append(max_digit)
            start_idx = max_idx + 1
            remaining_to_pick -= 1

        joltage = int("".join(result))
        total_joltage += joltage

    return total_joltage


if __name__ == "__main__":
    input_file = "input.txt"
    answer_part1 = solve_part1(input_file)
    answer_part2 = solve_part2(input_file)

    print(f"Part 1 - The answer is: {answer_part1}")
    print(f"Part 2 - The answer is: {answer_part2}")
