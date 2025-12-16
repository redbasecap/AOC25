use std::fs;

fn solve_part1(input_file: &str) -> u64 {
    let contents = fs::read_to_string(input_file).expect("Failed to read input file");
    
    let mut total_joltage: u64 = 0;
    
    for line in contents.lines() {
        let line = line.trim();
        if line.is_empty() {
            continue;
        }
        
        let chars: Vec<char> = line.chars().collect();
        let mut max_joltage: u64 = 0;
        
        // Try all pairs of positions (i, j) where i < j
        for i in 0..chars.len() {
            for j in (i + 1)..chars.len() {
                // Form the joltage from digits at positions i and j (in order)
                let joltage_str = format!("{}{}", chars[i], chars[j]);
                let joltage: u64 = joltage_str.parse().expect("Failed to parse joltage");
                max_joltage = max_joltage.max(joltage);
            }
        }
        
        total_joltage += max_joltage;
    }
    
    total_joltage
}

fn solve_part2(input_file: &str) -> u64 {
    let contents = fs::read_to_string(input_file).expect("Failed to read input file");
    
    let mut total_joltage: u64 = 0;
    let target_length = 12;
    
    for line in contents.lines() {
        let line = line.trim();
        if line.is_empty() {
            continue;
        }
        
        let chars: Vec<char> = line.chars().collect();
        let mut result = String::new();
        let mut start_idx = 0;
        let mut remaining_to_pick = target_length;
        
        for _ in 0..target_length {
            // How many digits can we skip?
            let available = chars.len() - start_idx;
            let can_skip = available - remaining_to_pick;
            
            // Find the maximum digit in the range we can pick from
            let mut max_digit = chars[start_idx];
            let mut max_idx = start_idx;
            
            for idx in start_idx..=(start_idx + can_skip) {
                if chars[idx] > max_digit {
                    max_digit = chars[idx];
                    max_idx = idx;
                }
            }
            
            result.push(max_digit);
            start_idx = max_idx + 1;
            remaining_to_pick -= 1;
        }
        
        let joltage: u64 = result.parse().expect("Failed to parse joltage");
        total_joltage += joltage;
    }
    
    total_joltage
}

fn main() {
    let input_file = "input.txt";
    
    let answer_part1 = solve_part1(input_file);
    let answer_part2 = solve_part2(input_file);
    
    println!("Part 1 - The answer is: {}", answer_part1);
    println!("Part 2 - The answer is: {}", answer_part2);
}
