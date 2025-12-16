"""
    solve_part1(input_file::String)::Int

Solve part 1: Count how many times the dial points at 0 after a rotation.
"""
function solve_part1(input_file::String)::Int
    lines = readlines(input_file)
    
    position = 50
    count_at_zero = 0
    
    for line in lines
        line = strip(line)
        if isempty(line)
            continue
        end
        
        direction = line[1]
        distance = parse(Int, line[2:end])
        
        if direction == 'L'
            position = mod(position - distance, 100)
        else  # direction == 'R'
            position = mod(position + distance, 100)
        end
        
        if position == 0
            count_at_zero += 1
        end
    end
    
    return count_at_zero
end

"""
    solve_part2(input_file::String)::Int

Solve part 2: Count every time the dial passes through 0, including during rotations.
"""
function solve_part2(input_file::String)::Int
    lines = readlines(input_file)
    
    position = 50
    count_at_zero = 0
    
    for line in lines
        line = strip(line)
        if isempty(line)
            continue
        end
        
        direction = line[1]
        distance = parse(Int, line[2:end])
        
        if direction == 'L'
            for _ in 1:distance
                position = mod(position - 1, 100)
                if position == 0
                    count_at_zero += 1
                end
            end
        else  # direction == 'R'
            for _ in 1:distance
                position = mod(position + 1, 100)
                if position == 0
                    count_at_zero += 1
                end
            end
        end
    end
    
    return count_at_zero
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
