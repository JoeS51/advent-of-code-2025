use std::fs;

fn main() {
    // let file_result = fs::read_to_string("sample-input").unwrap();
    let file_result = fs::read_to_string("inputs/day1-sample").unwrap();
    let mut curr_pos = 50;
    let mut total_zeroes = 0;
    for line in file_result.lines() {
        let dir = &line[0..1];
        let step = &line[1..];
        let direction: i32;
        if dir == "L" {
            direction = -1;
        } else {
            direction = 1
        }
        let step: i32 = step.parse().expect("not a num");
        
        curr_pos += (direction * step);
        curr_pos %= 100;
        
        if curr_pos == 0 {
            total_zeroes += 1;
        }

        println!("{line}");
        println!("{curr_pos}");
    }
    println!("{total_zeroes}");
}
