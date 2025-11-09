use std::fs;

fn main() {
    println!("Hello, world!");
    let file_result = fs::read_to_string("input1").unwrap();
    println!("{file_result}");
}
