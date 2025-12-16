use std::fs;

fn solve_part1(input_file: &str) -> usize {
    let contents = fs::read_to_string(input_file).expect("Failed to read input file");
    
    let mut ranges = Vec::new();
    let mut available_ids = Vec::new();
    let mut parsing_ranges = true;
    
    for line in contents.lines() {
        let line = line.trim();
        
        if line.is_empty() {
            parsing_ranges = false;
            continue;
        }
        
        if parsing_ranges {
            // Parse range (e.g., "3-5")
            let parts: Vec<&str> = line.split('-').collect();
            if parts.len() >= 2 {
                let start: u64 = parts[0].parse().unwrap_or(0);
                let end: u64 = parts[parts.len() - 1].parse().unwrap_or(0);
                ranges.push((start, end));
            }
        } else {
            // Parse available ID
            if let Ok(id) = line.parse::<u64>() {
                available_ids.push(id);
            }
        }
    }
    
    // Count fresh IDs
    let mut fresh_count = 0;
    for ingredient_id in available_ids {
        let is_fresh = ranges.iter().any(|(start, end)| {
            ingredient_id >= *start && ingredient_id <= *end
        });
        
        if is_fresh {
            fresh_count += 1;
        }
    }
    
    fresh_count
}

fn solve_part2(input_file: &str) -> u64 {
    let contents = fs::read_to_string(input_file).expect("Failed to read input file");
    
    let mut ranges = Vec::new();
    
    // Parse only the ranges (before blank line)
    for line in contents.lines() {
        let line = line.trim();
        
        if line.is_empty() {
            break;  // Stop at blank line
        }
        
        // Parse range (e.g., "3-5")
        let parts: Vec<&str> = line.split('-').collect();
        if parts.len() >= 2 {
            let start: u64 = parts[0].parse().unwrap_or(0);
            let end: u64 = parts[parts.len() - 1].parse().unwrap_or(0);
            ranges.push((start, end));
        }
    }
    
    // Sort ranges by start position
    ranges.sort();
    
    // Merge overlapping ranges
    let mut merged_ranges: Vec<(u64, u64)> = Vec::new();
    for (start, end) in ranges {
        if !merged_ranges.is_empty() && start <= merged_ranges[merged_ranges.len() - 1].1 + 1 {
            // Overlapping or adjacent, merge
            let last_idx = merged_ranges.len() - 1;
            let new_end = merged_ranges[last_idx].1.max(end);
            merged_ranges[last_idx] = (merged_ranges[last_idx].0, new_end);
        } else {
            // No overlap, add new range
            merged_ranges.push((start, end));
        }
    }
    
    // Count total IDs in merged ranges
    let mut total_count: u64 = 0;
    for (start, end) in merged_ranges {
        total_count += end - start + 1;
    }
    
    total_count
}

fn main() {
    let input_file = "input.txt";
    
    let answer_part1 = solve_part1(input_file);
    let answer_part2 = solve_part2(input_file);
    
    println!("Part 1 - The answer is: {}", answer_part1);
    println!("Part 2 - The answer is: {}", answer_part2);
}
