use std::fs;

fn is_invalid_id_part1(num: u64) -> bool {
    let s = num.to_string();
    
    // Number must have even length to be a repeated pattern
    if s.len() % 2 != 0 {
        return false;
    }
    
    // Check if first half equals second half
    let mid = s.len() / 2;
    let first_half = &s[..mid];
    let second_half = &s[mid..];
    
    first_half == second_half
}

fn is_invalid_id_part2(num: u64) -> bool {
    let s = num.to_string();
    
    // Try all possible pattern lengths
    for pattern_len in 1..=s.len() / 2 {
        let pattern = &s[..pattern_len];
        
        // Only valid if pattern length divides the string length evenly
        if s.len() % pattern_len != 0 {
            continue;
        }
        
        let expected_repetitions = s.len() / pattern_len;
        
        // Check if repeating pattern creates the number
        let repeated = pattern.repeat(expected_repetitions);
        if repeated == s && expected_repetitions >= 2 {
            return true;
        }
    }
    
    false
}

fn solve_part1(input_file: &str) -> u64 {
    let contents = fs::read_to_string(input_file).expect("Failed to read input file");
    let content = contents.trim();
    
    let mut total: u64 = 0;
    
    // Parse ranges separated by commas
    for range_str in content.split(',') {
        let parts: Vec<&str> = range_str.split('-').collect();
        if parts.len() != 2 {
            continue;
        }
        
        let start: u64 = parts[0].parse().expect("Failed to parse start");
        let end: u64 = parts[1].parse().expect("Failed to parse end");
        
        // Check each number in the range
        for num in start..=end {
            if is_invalid_id_part1(num) {
                total += num;
            }
        }
    }
    
    total
}

fn solve_part2(input_file: &str) -> u64 {
    let contents = fs::read_to_string(input_file).expect("Failed to read input file");
    let content = contents.trim();
    
    let mut total: u64 = 0;
    
    // Parse ranges separated by commas
    for range_str in content.split(',') {
        let parts: Vec<&str> = range_str.split('-').collect();
        if parts.len() != 2 {
            continue;
        }
        
        let start: u64 = parts[0].parse().expect("Failed to parse start");
        let end: u64 = parts[1].parse().expect("Failed to parse end");
        
        // Check each number in the range
        for num in start..=end {
            if is_invalid_id_part2(num) {
                total += num;
            }
        }
    }
    
    total
}

fn main() {
    let input_file = "input.txt";
    
    let answer_part1 = solve_part1(input_file);
    let answer_part2 = solve_part2(input_file);
    
    println!("Part 1 - The answer is: {}", answer_part1);
    println!("Part 2 - The answer is: {}", answer_part2);
}
