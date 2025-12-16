#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 6: Trash Compactor
Parse cephalopod math problems and solve them.
"""


def solve_part1(input_file):
    """
    Parse the worksheet and solve each problem.
    Each problem has numbers arranged vertically with an operation at the bottom.
    Problems are separated by full columns of spaces.
    """
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    
    # Find where numbers end and operations begin
    # The last line contains only operators
    operator_line = lines[-1]
    num_lines = lines[:-1]
    
    # Parse columns of problems
    # Each problem is separated by columns of spaces
    
    # First, identify problem boundaries by looking at the operator line
    problems = []
    in_problem = False
    problem_start = None
    
    for col in range(len(operator_line)):
        char = operator_line[col]
        
        if char in ['+', '*']:
            # We're in a problem
            if not in_problem:
                in_problem = True
                problem_start = col
            problem_end = col
        else:
            # We're in a gap
            if in_problem:
                # End of problem
                problems.append((problem_start, problem_end))
                in_problem = False
    
    # Don't forget the last problem if it ends at the end of the line
    if in_problem:
        problems.append((problem_start, problem_end))
    
    # Now parse each problem
    total = 0
    
    for start, end in problems:
        # Extract numbers from the column range
        numbers = []
        operator = None
        
        for row in range(len(num_lines)):
            line = num_lines[row]
            
            # Pad line if necessary
            if len(line) <= end:
                line = line + ' ' * (end - len(line) + 1)
            
            # Get character at this position
            char = line[start:end+1].strip()
            if char and char.isdigit():
                numbers.append(int(char))
        
        # Get operator from the operator line
        if len(operator_line) > end:
            operator = operator_line[end]
        
        # Evaluate the problem
        if numbers and operator:
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
    Placeholder for part 2.
    """
    return 0


if __name__ == "__main__":
    input_file = "input.txt"
    answer_part1 = solve_part1(input_file)
    answer_part2 = solve_part2(input_file)
    
    print(f"Part 1 - The answer is: {answer_part1}")
    print(f"Part 2 - The answer is: {answer_part2}")
