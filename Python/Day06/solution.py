#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 6: Trash Compactor
Parse cephalopod math problems and solve them.
"""


def solve_part1(input_file):
    """
    Parse the worksheet and solve each problem.
    Each problem has numbers arranged vertically with an operation at the bottom.
    Problems are separated by full columns of only spaces.
    """
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

    # Find max line length
    max_len = max(len(line) for line in lines)
    # Pad all lines to the same length
    lines = [line.ljust(max_len) for line in lines]

    operator_line = lines[-1]
    num_lines = lines[:-1]

    # Find separator columns (entirely spaces)
    separator_cols = set()
    for col in range(len(operator_line)):
        is_separator = True
        for row in range(len(num_lines)):
            if col < len(num_lines[row]) and num_lines[row][col] != " ":
                is_separator = False
                break
        if is_separator and col < len(operator_line) and operator_line[col] == " ":
            separator_cols.add(col)

    # Find problem boundaries
    problems = []
    problem_start = 0

    for col in range(len(operator_line) + 1):
        if col == len(operator_line) or col in separator_cols:
            if col > problem_start:
                # Find the operator in this range
                operator = None
                for op_col in range(problem_start, col):
                    if op_col < len(operator_line) and operator_line[op_col] in [
                        "+",
                        "*",
                    ]:
                        operator = operator_line[op_col]
                        break

                if operator:
                    problems.append((problem_start, col, operator))

            problem_start = col + 1

    # Now parse each problem
    total = 0

    for start, end, operator in problems:
        # Extract all numbers from this problem region
        numbers = []

        for row in range(len(num_lines)):
            line = num_lines[row]
            # Extract substring for this problem
            substring = line[start:end].strip()

            # Find all multi-digit numbers in this substring
            current_num = ""
            for char in substring:
                if char.isdigit():
                    current_num += char
                else:
                    if current_num:
                        numbers.append(int(current_num))
                        current_num = ""
            if current_num:
                numbers.append(int(current_num))

        # Evaluate the problem
        if numbers:
            result = numbers[0]
            for num in numbers[1:]:
                if operator == '+':
                    result += num
                elif operator == '*':
                    result *= num
            total += result

    return total


def solve_part2(input_file):
    """
    Read numbers right-to-left in columns.
    Each column represents one number (most significant digit at top).
    Process numbers right-to-left.
    """
    with open(input_file, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    # Find max line length
    max_len = max(len(line) for line in lines)
    # Pad all lines to the same length
    lines = [line.ljust(max_len) for line in lines]

    operator_line = lines[-1]
    num_lines = lines[:-1]

    # Find separator columns (entirely spaces)
    separator_cols = set()
    for col in range(len(operator_line)):
        is_separator = True
        for row in range(len(num_lines)):
            if col < len(num_lines[row]) and num_lines[row][col] != " ":
                is_separator = False
                break
        if is_separator and col < len(operator_line) and operator_line[col] == " ":
            separator_cols.add(col)

    # Find problem boundaries
    problems = []
    problem_start = 0

    for col in range(len(operator_line) + 1):
        if col == len(operator_line) or col in separator_cols:
            if col > problem_start:
                # Find the operator in this range
                operator = None
                for op_col in range(problem_start, col):
                    if op_col < len(operator_line) and operator_line[op_col] in [
                        "+",
                        "*",
                    ]:
                        operator = operator_line[op_col]
                        break

                if operator:
                    problems.append((problem_start, col, operator))

            problem_start = col + 1

    # Now parse each problem (reading columns right-to-left)
    total = 0

    for start, end, operator in problems:
        # Find which columns in this range are non-space (digit columns)
        digit_cols = []
        for col in range(start, end):
            is_space_col = True
            for row in range(len(num_lines)):
                if col < len(num_lines[row]) and num_lines[row][col] != " ":
                    is_space_col = False
                    break
            if not is_space_col:
                digit_cols.append(col)

        # Form numbers from each digit column (top to bottom)
        numbers = []
        for col in digit_cols:
            num_str = ""
            for row in range(len(num_lines)):
                if col < len(num_lines[row]) and num_lines[row][col].isdigit():
                    num_str += num_lines[row][col]
            if num_str:
                numbers.append(int(num_str))

        # Process numbers right-to-left (reverse them)
        numbers.reverse()

        # Evaluate
        if numbers:
            result = numbers[0]
            for num in numbers[1:]:
                if operator == "+":
                    result += num
                elif operator == "*":
                    result *= num
            total += result

    return total


if __name__ == "__main__":
    input_file = "input.txt"
    answer_part1 = solve_part1(input_file)
    answer_part2 = solve_part2(input_file)
    
    print(f"Part 1 - The answer is: {answer_part1}")
    print(f"Part 2 - The answer is: {answer_part2}")
