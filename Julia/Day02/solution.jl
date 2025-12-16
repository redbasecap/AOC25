"""
    is_invalid_id_part1(num::Int)::Bool

Check if a number is an invalid ID (Part 1).
Invalid IDs are made of a sequence of digits repeated exactly twice.
Examples: 55 (5 twice), 6464 (64 twice), 123123 (123 twice)
"""
function is_invalid_id_part1(num::Int)::Bool
    s = string(num)
    
    # Number must have even length to be a repeated pattern
    if length(s) % 2 != 0
        return false
    end
    
    # Check if first half equals second half
    mid = div(length(s), 2)
    first_half = s[1:mid]
    second_half = s[mid+1:end]
    
    return first_half == second_half
end

"""
    is_invalid_id_part2(num::Int)::Bool

Check if a number is an invalid ID (Part 2).
Invalid IDs are made of a sequence of digits repeated at least twice.
Examples: 11 (1 twice), 111 (1 thrice), 123123 (123 twice)
"""
function is_invalid_id_part2(num::Int)::Bool
    s = string(num)
    
    # Try all possible pattern lengths
    for pattern_len in 1:div(length(s), 2)
        pattern = s[1:pattern_len]
        
        # Only valid if pattern length divides the string length evenly
        if length(s) % pattern_len != 0
            continue
        end
        
        expected_repetitions = div(length(s), pattern_len)
        
        # Check if repeating pattern creates the number
        repeated = pattern ^ expected_repetitions
        if repeated == s && expected_repetitions >= 2
            return true
        end
    end
    
    return false
end

"""
    solve_part1(input_file::String)::Int

Find all invalid IDs in the given ranges (Part 1) and sum them up.
"""
function solve_part1(input_file::String)::Int
    content = read(input_file, String)
    content = strip(content)
    
    # Parse ranges
    ranges = split(content, ',')
    
    total = 0
    
    for range_str in ranges
        parts = split(range_str, '-')
        start = parse(Int, parts[1])
        stop = parse(Int, parts[2])
        
        # Check each number in the range
        for num in start:stop
            if is_invalid_id_part1(num)
                total += num
            end
        end
    end
    
    return total
end

"""
    solve_part2(input_file::String)::Int

Find all invalid IDs in the given ranges (Part 2) and sum them up.
"""
function solve_part2(input_file::String)::Int
    content = read(input_file, String)
    content = strip(content)
    
    # Parse ranges
    ranges = split(content, ',')
    
    total = 0
    
    for range_str in ranges
        parts = split(range_str, '-')
        start = parse(Int, parts[1])
        stop = parse(Int, parts[2])
        
        # Check each number in the range
        for num in start:stop
            if is_invalid_id_part2(num)
                total += num
            end
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
