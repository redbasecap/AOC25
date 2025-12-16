use std::fs;

fn solve_part1(input_file: &str) -> usize {
    let contents = fs::read_to_string(input_file).expect("Failed to read input file");
    
    let mut position: i32 = 50;
    let mut count_at_zero = 0;
    
    for line in contents.lines() {
        let line = line.trim();
        if line.is_empty() {
            continue;
        }
        
        let direction = line.chars().next().unwrap();
        let distance: i32 = line[1..].parse().expect("Failed to parse distance");
        
        if direction == 'L' {
            position = ((position - distance) % 100 + 100) % 100;
        } else {
            position = (position + distance) % 100;
        }
        
        if position == 0 {
            count_at_zero += 1;
        }
    }
    
    count_at_zero
}

fn solve_part2(input_file: &str) -> usize {
    let contents = fs::read_to_string(input_file).expect("Failed to read input file");
    
    let mut position: i32 = 50;
    let mut count_at_zero = 0;
    
    for line in contents.lines() {
        let line = line.trim();
        if line.is_empty() {
            continue;
        }
        
        let direction = line.chars().next().unwrap();
        let distance: i32 = line[1..].parse().expect("Failed to parse distance");
        
        if direction == 'L' {
            for _ in 0..distance {
                position = ((position - 1) % 100 + 100) % 100;
                if position == 0 {
                    count_at_zero += 1;
                }
            }
        } else {
            for _ in 0..distance {
                position = (position + 1) % 100;
                if position == 0 {
                    count_at_zero += 1;
                }
            }
        }
    }
    
    count_at_zero
}

fn main() {
    let input_file = "input.txt";
    
    let answer_part1 = solve_part1(input_file);
    let answer_part2 = solve_part2(input_file);
    
    println!("Part 1 - The answer is: {}", answer_part1);
    println!("Part 2 - The answer is: {}", answer_part2);
}
