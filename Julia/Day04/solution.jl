"""
    get_accessible_rolls(grid::Vector{String})::Vector{Tuple{Int, Int}}

Find all rolls that can be accessed (have fewer than 4 neighbors).
"""
function get_accessible_rolls(grid::Vector{String})::Vector{Tuple{Int, Int}}
    rows = length(grid)
    cols = rows > 0 ? length(grid[1]) : 0
    
    # Direction vectors for 8 neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    accessible = Tuple{Int, Int}[]
    
    for r in 1:rows
        for c in 1:cols
            # Only check rolls of paper (@)
            if grid[r][c] == '@'
                # Count adjacent rolls
                adjacent_rolls = 0
                for (dr, dc) in directions
                    nr = r + dr
                    nc = c + dc
                    
                    # Check bounds
                    if 1 <= nr <= rows && 1 <= nc <= cols
                        if grid[nr][nc] == '@'
                            adjacent_rolls += 1
                        end
                    end
                end
                
                # Can be accessed if fewer than 4 adjacent rolls
                if adjacent_rolls < 4
                    push!(accessible, (r, c))
                end
            end
        end
    end
    
    return accessible
end

"""
    solve_part1(input_file::String)::Int

Count how many rolls of paper (@) can be accessed.
A roll can be accessed if it has fewer than 4 rolls in its 8 neighbors.
"""
function solve_part1(input_file::String)::Int
    lines = readlines(input_file)
    grid = [line for line in lines if !isempty(strip(line))]
    
    accessible = get_accessible_rolls(grid)
    return length(accessible)
end

"""
    solve_part2(input_file::String)::Int

Repeatedly find and remove accessible rolls until no more can be removed.
"""
function solve_part2(input_file::String)::Int
    lines = readlines(input_file)
    grid = [collect(line) for line in lines if !isempty(strip(line))]
    
    total_removed = 0
    
    # Keep removing rolls while there are accessible ones
    while true
        grid_str = [String(row) for row in grid]
        accessible = get_accessible_rolls(grid_str)
        
        if isempty(accessible)
            break
        end
        
        # Remove all accessible rolls
        for (r, c) in accessible
            grid[r][c] = '.'
            total_removed += 1
        end
    end
    
    return total_removed
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
