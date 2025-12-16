"""
    solve_part1(input_file::String)::Int

Parse the worksheet and solve each problem.
Each problem has numbers arranged vertically with an operation at the bottom.
Problems are separated by full columns of only spaces.
"""
function solve_part1(input_file::String)::Int
    lines = readlines(input_file)
    
    # Find max line length
    max_len = maximum(length.(lines))
    # Pad all lines to the same length
    lines = [line * " " ^ (max_len - length(line)) for line in lines]
    
    operator_line = lines[end]
    num_lines = lines[1:end-1]
    
    # Find separator columns (entirely spaces)
    separator_cols = Set{Int}()
    for col in 1:max_len
        is_separator = true
        for row in 1:length(num_lines)
            if col <= length(num_lines[row]) && num_lines[row][col] != ' '
                is_separator = false
                break
            end
        end
        if is_separator && (col > length(operator_line) || operator_line[col] == ' ')
            push!(separator_cols, col)
        end
    end
    
    # Find problem boundaries
    problems = Tuple{Int, Int, Char}[]
    problem_start = 1
    
    for col in 1:(length(operator_line)+1)
        if col == length(operator_line) + 1 || col in separator_cols
            if col > problem_start
                # Find the operator in this range
                operator = ' '
                for op_col in problem_start:col-1
                    if op_col <= length(operator_line) && operator_line[op_col] in ['+', '*']
                        operator = operator_line[op_col]
                        break
                    end
                end
                
                if operator in ['+', '*']
                    push!(problems, (problem_start, col, operator))
                end
            end
            
            problem_start = col + 1
        end
    end
    
    # Parse each problem
    total = 0
    
    for (start, stop, operator) in problems
        numbers = Int[]
        
        # Extract all numbers from this problem region
        for row in 1:length(num_lines)
            line = num_lines[row]
            substring = if stop <= length(line)
                line[start:stop-1]
            elseif start <= length(line)
                line[start:end]
            else
                ""
            end
            
            # Find all multi-digit numbers in this substring
            current_num = ""
            for char in substring
                if isdigit(char)
                    current_num *= char
                else
                    if !isempty(current_num)
                        push!(numbers, parse(Int, current_num))
                        current_num = ""
                    end
                end
            end
            if !isempty(current_num)
                push!(numbers, parse(Int, current_num))
            end
        end
        
        # Evaluate
        if !isempty(numbers)
            result = numbers[1]
            for num in numbers[2:end]
                if operator == '+'
                    result += num
                else
                    result *= num
                end
            end
            total += result
        end
    end
    
    return total
end

"""
    solve_part2(input_file::String)::Int

Read numbers right-to-left in columns.
Each column represents one number (most significant digit at top).
Process numbers right-to-left.
"""
function solve_part2(input_file::String)::Int
    lines = readlines(input_file)
    
    # Find max line length
    max_len = maximum(length.(lines))
    # Pad all lines to the same length
    lines = [line * " " ^ (max_len - length(line)) for line in lines]
    
    operator_line = lines[end]
    num_lines = lines[1:end-1]
    
    # Find separator columns (entirely spaces)
    separator_cols = Set{Int}()
    for col in 1:max_len
        is_separator = true
        for row in 1:length(num_lines)
            if col <= length(num_lines[row]) && num_lines[row][col] != ' '
                is_separator = false
                break
            end
        end
        if is_separator && (col > length(operator_line) || operator_line[col] == ' ')
            push!(separator_cols, col)
        end
    end
    
    # Find problem boundaries
    problems = Tuple{Int, Int, Char}[]
    problem_start = 1
    
    for col in 1:(length(operator_line)+1)
        if col == length(operator_line) + 1 || col in separator_cols
            if col > problem_start
                # Find the operator in this range
                operator = ' '
                for op_col in problem_start:col-1
                    if op_col <= length(operator_line) && operator_line[op_col] in ['+', '*']
                        operator = operator_line[op_col]
                        break
                    end
                end
                
                if operator in ['+', '*']
                    push!(problems, (problem_start, col, operator))
                end
            end
            
            problem_start = col + 1
        end
    end
    
    # Parse each problem (reading columns right-to-left)
    total = 0
    
    for (start, stop, operator) in problems
        # Find which columns in this range are non-space (digit columns)
        digit_cols = Int[]
        for col in start:(stop-1)
            is_space_col = true
            for row in 1:length(num_lines)
                line = num_lines[row]
                if col <= length(line) && line[col] != ' '
                    is_space_col = false
                    break
                end
            end
            if !is_space_col
                push!(digit_cols, col)
            end
        end
        
        # Form numbers from each digit column (top to bottom)
        numbers = Int[]
        for col in digit_cols
            num_str = ""
            for row in 1:length(num_lines)
                line = num_lines[row]
                if col <= length(line) && isdigit(line[col])
                    num_str *= line[col]
                end
            end
            if !isempty(num_str)
                push!(numbers, parse(Int, num_str))
            end
        end
        
        # Process numbers right-to-left (reverse them)
        reverse!(numbers)
        
        # Evaluate
        if !isempty(numbers)
            result = numbers[1]
            for num in numbers[2:end]
                if operator == '+'
                    result += num
                else
                    result *= num
                end
            end
            total += result
        end
    end
    
    return total
end

"""
    main()

Main entry point: solve both parts and print results.
"""
function main()
    input_file = "input.txt"
    
    answer_part1 = solve_part1(input_file)
    answer_part2 = solve_part2(input_file)
    
    println("Part 1 - The answer is: $answer_part1")
    println("Part 2 - The answer is: $answer_part2")
end

# Run if executed as script
if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
