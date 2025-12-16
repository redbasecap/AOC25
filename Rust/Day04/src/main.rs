use std::fs;

fn get_accessible_rolls(grid: &[Vec<char>]) -> Vec<(usize, usize)> {
    let rows = grid.len();
    let cols = if rows > 0 { grid[0].len() } else { 0 };
    
    // Direction vectors for 8 neighbors
    let directions: [(i32, i32); 8] = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ];
    
    let mut accessible = Vec::new();
    
    for r in 0..rows {
        for c in 0..cols {
            // Only check rolls of paper (@)
            if grid[r][c] == '@' {
                // Count adjacent rolls
                let mut adjacent_rolls = 0;
                for (dr, dc) in &directions {
                    let nr = (r as i32 + dr) as usize;
                    let nc = (c as i32 + dc) as usize;
                    
                    // Check bounds
                    if (r as i32 + dr) >= 0 && (r as i32 + dr) < rows as i32
                        && (c as i32 + dc) >= 0 && (c as i32 + dc) < cols as i32
                    {
                        if grid[nr][nc] == '@' {
                            adjacent_rolls += 1;
                        }
                    }
                }
                
                // Can be accessed if fewer than 4 adjacent rolls
                if adjacent_rolls < 4 {
                    accessible.push((r, c));
                }
            }
        }
    }
    
    accessible
}

fn solve_part1(input_file: &str) -> usize {
    let contents = fs::read_to_string(input_file).expect("Failed to read input file");
    
    let grid: Vec<Vec<char>> = contents
        .lines()
        .map(|line| line.chars().collect())
        .collect();
    
    get_accessible_rolls(&grid).len()
}

fn solve_part2(input_file: &str) -> usize {
    let contents = fs::read_to_string(input_file).expect("Failed to read input file");
    
    let mut grid: Vec<Vec<char>> = contents
        .lines()
        .map(|line| line.chars().collect())
        .collect();
    
    let mut total_removed = 0;
    
    // Keep removing rolls while there are accessible ones
    loop {
        let accessible = get_accessible_rolls(&grid);
        
        if accessible.is_empty() {
            break;
        }
        
        // Remove all accessible rolls
        for (r, c) in accessible {
            grid[r][c] = '.';
            total_removed += 1;
        }
    }
    
    total_removed
}

fn main() {
    let input_file = "input.txt";
    
    let answer_part1 = solve_part1(input_file);
    let answer_part2 = solve_part2(input_file);
    
    println!("Part 1 - The answer is: {}", answer_part1);
    println!("Part 2 - The answer is: {}", answer_part2);
}
