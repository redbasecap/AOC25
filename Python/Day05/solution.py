#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 5: Cafeteria
Determine which ingredient IDs are fresh based on given ranges.
"""


def solve_part1(input_file):
    """
    Count how many available ingredient IDs are fresh.
    An ID is fresh if it falls into at least one of the fresh ranges.
    """
    with open(input_file, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    # Parse input: ranges first, then blank line, then available IDs
    ranges = []
    available_ids = []
    parsing_ranges = True

    for line in lines:
        if not line.strip():  # Blank line separates ranges from IDs
            parsing_ranges = False
            continue

        if parsing_ranges:
            # Parse range (e.g., "3-5")
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        else:
            # Parse available ID
            available_ids.append(int(line))

    # Count fresh IDs
    fresh_count = 0
    for ingredient_id in available_ids:
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        if is_fresh:
            fresh_count += 1

    return fresh_count


def solve_part2(input_file):
    """
    Count total ingredient IDs considered fresh by the ranges.
    Merge overlapping ranges and count all IDs within them.
    """
    with open(input_file, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    # Parse only the ranges (before blank line)
    ranges = []
    for line in lines:
        if not line.strip():  # Stop at blank line
            break

        # Parse range (e.g., "3-5")
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    # Sort ranges by start position
    ranges.sort()

    # Merge overlapping ranges
    merged_ranges = []
    for start, end in ranges:
        if merged_ranges and start <= merged_ranges[-1][1] + 1:
            # Overlapping or adjacent, merge
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
        else:
            # No overlap, add new range
            merged_ranges.append((start, end))

    # Count total IDs in merged ranges
    total_count = 0
    for start, end in merged_ranges:
        total_count += end - start + 1

    return total_count


if __name__ == "__main__":
    input_file = "input.txt"
    answer_part1 = solve_part1(input_file)
    answer_part2 = solve_part2(input_file)

    print(f"Part 1 - The answer is: {answer_part1}")
    print(f"Part 2 - The answer is: {answer_part2}")
