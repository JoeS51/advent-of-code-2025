use std::fs;

fn main() {
    let file_result = fs::read_to_string("inputs/day1-actual").unwrap();
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
        
        let prev_pos = curr_pos;
        curr_pos += direction * step;

        if curr_pos < prev_pos {
            for i in (curr_pos..prev_pos) {
                let m = i%100;
                if i % 100 == 0 {
                    total_zeroes += 1
                }
            }
        } else {
            for i in prev_pos+1..=curr_pos {
                let m = i%100;
                if i % 100 == 0 {
                    total_zeroes += 1
                }
            }
        }

        curr_pos %= 100;

    }
    println!("total zeroes is {total_zeroes}");
}
