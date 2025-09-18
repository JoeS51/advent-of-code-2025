use std::io;
use rand::Rng;

fn main() {
    println!("Insert your guess hehehe");
    println!();

    let secret_num = rand::thread_rng().gen_range(1..=100);

    println!("secret num {secret_num}");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("error dog");
    
    println!("Your number was {guess}")
}
