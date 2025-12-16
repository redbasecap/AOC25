use std::fs;

fn solve_part1(input_file: &str) -> u64 {
    let contents = fs::read_to_string(input_file).expect("Failed to read input file");
    let lines: Vec<&str> = contents.lines().collect();
    
    let operator_line = lines[lines.len() - 1];
    let num_lines = &lines[..lines.len() - 1];
    
    // Find max line length
    let max_len = lines.iter().map(|l| l.len()).max().unwrap_or(0);
    
    // Find separator columns (entirely spaces)
    let mut separator_cols = std::collections::HashSet::new();
    for col in 0..max_len {
        let mut is_separator = true;
        for row in 0..num_lines.len() {
            let line = num_lines[row];
            if col < line.len() && line.chars().nth(col).unwrap_or(' ') != ' ' {
                is_separator = false;
                break;
            }
        }
        if is_separator && (col >= operator_line.len() || operator_line.chars().nth(col).unwrap_or(' ') == ' ') {
            separator_cols.insert(col);
        }
    }
    
    // Find problem boundaries
    let mut problems = Vec::new();
    let mut problem_start = 0;
    
    for col in 0..=operator_line.len() {
        if col == operator_line.len() || separator_cols.contains(&col) {
            if col > problem_start {
                // Find the operator in this range
                let mut operator = ' ';
                for op_col in problem_start..col {
                    if let Some(c) = operator_line.chars().nth(op_col) {
                        if c == '+' || c == '*' {
                            operator = c;
                            break;
                        }
                    }
                }
                
                if operator == '+' || operator == '*' {
                    problems.push((problem_start, col, operator));
                }
            }
            
            problem_start = col + 1;
        }
    }
    
    let mut total: u64 = 0;
    
    for (start, end, operator) in problems {
        let mut numbers = Vec::new();
        
        // Extract all numbers from this problem region
        for row in 0..num_lines.len() {
            let line = num_lines[row];
            let substring = if end <= line.len() {
                &line[start..end]
            } else if start < line.len() {
                &line[start..]
            } else {
                ""
            };
            
            // Find all multi-digit numbers in this substring
            let mut current_num = String::new();
            for ch in substring.chars() {
                if ch.is_numeric() {
                    current_num.push(ch);
                } else {
                    if !current_num.is_empty() {
                        if let Ok(num) = current_num.parse::<u64>() {
                            numbers.push(num);
                        }
                        current_num.clear();
                    }
                }
            }
            if !current_num.is_empty() {
                if let Ok(num) = current_num.parse::<u64>() {
                    numbers.push(num);
                }
            }
        }
        
        // Evaluate
        if !numbers.is_empty() {
            let mut result = numbers[0];
            for num in &numbers[1..] {
                if operator == '+' {
                    result += num;
                } else {
                    result *= num;
                }
            }
            total += result;
        }
    }
    
    total
}

fn solve_part2(input_file: &str) -> u64 {
    let contents = fs::read_to_string(input_file).expect("Failed to read input file");
    let lines: Vec<&str> = contents.lines().collect();
    
    let operator_line = lines[lines.len() - 1];
    let num_lines = &lines[..lines.len() - 1];
    
    // Find max line length
    let max_len = lines.iter().map(|l| l.len()).max().unwrap_or(0);
    
    // Find separator columns (entirely spaces)
    let mut separator_cols = std::collections::HashSet::new();
    for col in 0..max_len {
        let mut is_separator = true;
        for row in 0..num_lines.len() {
            let line = num_lines[row];
            if col < line.len() && line.chars().nth(col).unwrap_or(' ') != ' ' {
                is_separator = false;
                break;
            }
        }
        if is_separator && (col >= operator_line.len() || operator_line.chars().nth(col).unwrap_or(' ') == ' ') {
            separator_cols.insert(col);
        }
    }
    
    // Find problem boundaries
    let mut problems = Vec::new();
    let mut problem_start = 0;
    
    for col in 0..=operator_line.len() {
        if col == operator_line.len() || separator_cols.contains(&col) {
            if col > problem_start {
                // Find the operator in this range
                let mut operator = ' ';
                for op_col in problem_start..col {
                    if let Some(c) = operator_line.chars().nth(op_col) {
                        if c == '+' || c == '*' {
                            operator = c;
                            break;
                        }
                    }
                }
                
                if operator == '+' || operator == '*' {
                    problems.push((problem_start, col, operator));
                }
            }
            
            problem_start = col + 1;
        }
    }
    
    let mut total: u64 = 0;
    
    for (start, end, operator) in problems {
        // Find which columns in this range are non-space (digit columns)
        let mut digit_cols = Vec::new();
        for col in start..end {
            let mut is_space_col = true;
            for row in 0..num_lines.len() {
                let line = num_lines[row];
                if col < line.len() && line.chars().nth(col).unwrap_or(' ') != ' ' {
                    is_space_col = false;
                    break;
                }
            }
            if !is_space_col {
                digit_cols.push(col);
            }
        }
        
        // Form numbers from each digit column (top to bottom)
        let mut numbers = Vec::new();
        for col in digit_cols {
            let mut num_str = String::new();
            for row in 0..num_lines.len() {
                let line = num_lines[row];
                if col < line.len() {
                    if let Some(ch) = line.chars().nth(col) {
                        if ch.is_numeric() {
                            num_str.push(ch);
                        }
                    }
                }
            }
            if !num_str.is_empty() {
                if let Ok(num) = num_str.parse::<u64>() {
                    numbers.push(num);
                }
            }
        }
        
        // Process numbers right-to-left (reverse them)
        numbers.reverse();
        
        // Evaluate
        if !numbers.is_empty() {
            let mut result = numbers[0];
            for num in &numbers[1..] {
                if operator == '+' {
                    result += num;
                } else {
                    result *= num;
                }
            }
            total += result;
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
