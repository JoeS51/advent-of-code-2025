use std::io;
use rand::Rng;

use std::cmp::Ordering;

fn main() {
    println!("Insert your guess hehehe");
    println!();

    let secret_num = rand::thread_rng().gen_range(1..=100);


    loop {
        println!("guess");
        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("error dog");
        
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("Your number was {guess}");

        match guess.cmp(&secret_num) {
            Ordering::Less => println!("too small"),
            Ordering::Greater => println!("too big"),
            Ordering::Equal => {
                println!("nice");
                break;
            }
        }
    }
}
