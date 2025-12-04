use std::fs;

fn main() {
    //let file_result = fs::read_to_string("inputs/day2-sample").unwrap();
    let file_result = fs::read_to_string("inputs/day2-actual").unwrap();
    let ranges: Vec<&str> = file_result.split(',').collect();
    let mut sum: u64 = 0;
    for range in ranges {
        let nums: Vec<&str> = range.split('-').collect();
        let start: u64 = nums[0].parse().expect("not a num");
        let end: u64 = nums[1].parse().expect("not a num");
        for i in start..=end {
            // do string slicing to compare first half with second half
            let string_representation: String = i.to_string();
            let length = string_representation.len();
            let half = length / 2;
            for possible_len in 1..=half {
                if length % possible_len != 0 {
                    continue
                }
                let substr_to_repeat = &string_representation[0..possible_len];
                let repeated_str = substr_to_repeat.repeat(length / possible_len);
                if repeated_str == string_representation {
                    sum += i;
                    break;
                }
            }
        }
    }
    println!("SUM IS {sum}");
}
