"""
    solve_part1(input_file::String)::Int

Count how many available ingredient IDs are fresh.
An ID is fresh if it falls into at least one of the fresh ranges.
"""
function solve_part1(input_file::String)::Int
    lines = readlines(input_file)
    
    ranges = Tuple{Int, Int}[]
    available_ids = Int[]
    parsing_ranges = true
    
    for line in lines
        line = strip(line)
        
        if isempty(line)
            parsing_ranges = false
            continue
        end
        
        if parsing_ranges
            # Parse range (e.g., "3-5")
            parts = split(line, '-')
            if length(parts) >= 2
                start = parse(Int, parts[1])
                stop = parse(Int, parts[end])
                push!(ranges, (start, stop))
            end
        else
            # Parse available ID
            try
                id = parse(Int, line)
                push!(available_ids, id)
            catch
            end
        end
    end
    
    # Count fresh IDs
    fresh_count = 0
    for ingredient_id in available_ids
        is_fresh = false
        for (start, stop) in ranges
            if start <= ingredient_id <= stop
                is_fresh = true
                break
            end
        end
        if is_fresh
            fresh_count += 1
        end
    end
    
    return fresh_count
end

"""
    solve_part2(input_file::String)::Int

Count total ingredient IDs considered fresh by the ranges.
Merge overlapping ranges and count all IDs within them.
"""
function solve_part2(input_file::String)::Int
    lines = readlines(input_file)
    
    ranges = Tuple{Int, Int}[]
    
    # Parse only the ranges (before blank line)
    for line in lines
        line = strip(line)
        
        if isempty(line)
            break  # Stop at blank line
        end
        
        # Parse range (e.g., "3-5")
        parts = split(line, '-')
        if length(parts) >= 2
            start = parse(Int, parts[1])
            stop = parse(Int, parts[end])
            push!(ranges, (start, stop))
        end
    end
    
    # Sort ranges by start position
    sort!(ranges)
    
    # Merge overlapping ranges
    merged_ranges = Tuple{Int, Int}[]
    for (start, stop) in ranges
        if !isempty(merged_ranges) && start <= merged_ranges[end][2] + 1
            # Overlapping or adjacent, merge
            last = pop!(merged_ranges)
            push!(merged_ranges, (last[1], max(last[2], stop)))
        else
            # No overlap, add new range
            push!(merged_ranges, (start, stop))
        end
    end
    
    # Count total IDs in merged ranges
    total_count = 0
    for (start, stop) in merged_ranges
        total_count += stop - start + 1
    end
    
    return total_count
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
