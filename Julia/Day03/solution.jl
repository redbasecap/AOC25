"""
    solve_part1(input_file::String)::Int

For each bank (line), find the pair of digits at positions i < j that forms
the maximum joltage. You cannot rearrange batteries.
Sum all the maximum joltages.
"""
function solve_part1(input_file::String)::Int
    lines = readlines(input_file)
    
    total_joltage = 0
    
    for line in lines
        line = strip(line)
        if isempty(line)
            continue
        end
        
        # Try all pairs of positions (i, j) where i < j
        max_joltage = 0
        for i in 1:length(line)
            for j in (i+1):length(line)
                # Form the joltage from digits at positions i and j (in order)
                joltage_str = string(line[i], line[j])
                joltage = parse(Int, joltage_str)
                max_joltage = max(max_joltage, joltage)
            end
        end
        
        total_joltage += max_joltage
    end
    
    return total_joltage
end

"""
    solve_part2(input_file::String)::Int

For each bank (line), find the largest 12-digit joltage by selecting
12 batteries while maintaining their order.
Use a greedy algorithm: for each position, pick the largest digit
that still leaves enough digits to complete the selection.
"""
function solve_part2(input_file::String)::Int
    lines = readlines(input_file)
    
    total_joltage = 0
    target_length = 12
    
    for line in lines
        line = strip(line)
        if isempty(line)
            continue
        end
        
        # Greedy approach: for each position in result, find the largest digit
        result = Char[]
        start_idx = 1  # Julia uses 1-based indexing
        remaining_to_pick = target_length
        
        for _ in 1:target_length
            # How many digits can we skip?
            available = length(line) - start_idx + 1
            can_skip = available - remaining_to_pick
            
            # Find the maximum digit in the range we can pick from
            max_digit = line[start_idx]
            max_idx = start_idx
            
            for idx in start_idx:(start_idx + can_skip)
                if line[idx] > max_digit
                    max_digit = line[idx]
                    max_idx = idx
                end
            end
            
            push!(result, max_digit)
            start_idx = max_idx + 1
            remaining_to_pick -= 1
        end
        
        joltage = parse(Int, String(result))
        total_joltage += joltage
    end
    
    return total_joltage
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
