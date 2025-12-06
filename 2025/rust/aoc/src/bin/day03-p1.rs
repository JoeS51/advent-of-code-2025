use std::fs;

fn main() {
    // let file_result = fs::read_to_string("inputs/day3-sample").unwrap();
    let file_result = fs::read_to_string("inputs/day3-actual").unwrap();
    let mut total = 0;
    for line in file_result.lines() {
        let mut tens_place = 0;
        let mut ones_place = 0;
        for (i, num) in line.chars().enumerate() {
            let curr_num: u32 = num.to_digit(10).expect("expected num");
            let is_last = i == line.len() - 1;
            if (curr_num > tens_place && !is_last) {
                tens_place = curr_num;
                ones_place = 0;
            } else {
                ones_place = u32::max(ones_place, curr_num);
            }
        }
        let result = (tens_place * 10) + ones_place;
        total += result 
    }
    println!("{total}");
}
