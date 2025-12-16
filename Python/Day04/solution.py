#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 4: Printing Department
Count rolls of paper that can be accessed by forklifts.
A roll can be accessed if fewer than 4 rolls are in the 8 adjacent positions.
"""


def count_accessible_rolls(grid):
    """
    Count and return positions of accessible rolls.
    A roll can be accessed if it has fewer than 4 rolls in its 8 neighbors.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Direction vectors for 8 neighbors
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    accessible = []

    for r in range(rows):
        for c in range(cols):
            # Only check rolls of paper (@)
            if grid[r][c] == "@":
                # Count adjacent rolls
                adjacent_rolls = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check bounds
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "@":
                            adjacent_rolls += 1

                # Can be accessed if fewer than 4 adjacent rolls
                if adjacent_rolls < 4:
                    accessible.append((r, c))

    return accessible


def solve_part1(input_file):
    """
    Count how many rolls of paper (@) can be accessed.
    A roll can be accessed if it has fewer than 4 rolls in its 8 neighbors.
    """
    with open(input_file, "r") as f:
        grid = [line.rstrip("\n") for line in f.readlines()]

    accessible = count_accessible_rolls(grid)
    return len(accessible)


def solve_part2(input_file):
    """
    Repeatedly find and remove accessible rolls until no more can be removed.
    """
    with open(input_file, "r") as f:
        grid = [list(line.rstrip("\n")) for line in f.readlines()]

    total_removed = 0

    # Keep removing rolls while there are accessible ones
    while True:
        # Create string version for counting
        grid_str = ["".join(row) for row in grid]
        accessible = count_accessible_rolls(grid_str)

        if not accessible:
            break

        # Remove all accessible rolls
        for r, c in accessible:
            grid[r][c] = "."
            total_removed += 1

    return total_removed


if __name__ == "__main__":
    input_file = "input.txt"
    answer_part1 = solve_part1(input_file)
    answer_part2 = solve_part2(input_file)

    print(f"Part 1 - The answer is: {answer_part1}")
    print(f"Part 2 - The answer is: {answer_part2}")
