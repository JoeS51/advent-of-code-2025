use std::fs;

fn main() {
    let file_result = fs::read_to_string("input2").unwrap();
    let mut sum = 0;
    let mut found_first_digit= false;
    let mut first_digit = '1';
    let mut last_digit = '2';
    for line in file_result.chars() {
        if line == '\n' {
            found_first_digit = false;
            let combined = first_digit.to_string() + &last_digit.to_string();
            let combined_num: i32 = combined.parse().expect("not a num");
            sum += combined_num;
        } else {
            if line.is_ascii_digit() {
                if !found_first_digit {
                    found_first_digit = true;
                    first_digit = line;
                }
                last_digit = line;
            }
        }
    }
    println!("SUM IS {sum}");
}
