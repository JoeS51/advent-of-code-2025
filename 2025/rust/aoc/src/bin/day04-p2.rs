use std::fs;

const DIRS: [(isize, isize); 8] = [
    (-1, -1), (-1, 0), (0, -1), (1, 1), (1, 0), (0, 1), (-1, 1), (1, -1)
];

fn main() {
    // let file_result = fs::read_to_string("inputs/day4-sample").unwrap();
    let file_result = fs::read_to_string("inputs/day4-actual").unwrap();
    let mut grid: Vec<Vec<char>> = file_result
        .lines()
        .map(|line| line.chars().collect())
        .collect();

    let mut ans = 0;
    let m = grid.len();
    let n = grid[0].len();

    let mut new_grid: Vec<Vec<char>> = vec![vec!['.'; n]; m];
    let mut changed = 1;
    // println!("{:?}", grid);
    while changed != 0 {
        changed = 0;
        new_grid = vec![vec!['.'; n]; m];

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] != '.' && isValid(i, j, m, n, &grid) {
                    ans += 1;
                    changed += 1;
                } else if grid[i][j] == '@' {
                    new_grid[i][j] = '@';
                }
            }
        }
        println!("{:?}", new_grid);
        grid = new_grid.clone();
    }

    println!("Answer is: {ans}");

}

fn isValid(i: usize, j: usize, m: usize, n: usize, grid: &Vec<Vec<char>>) -> bool {
    let mut adj = 0;
    for (dx, dy) in DIRS {
        let new_i = i as isize - dx;
        let new_j = j as isize - dy;
        let size_i = new_i as usize;
        let size_j = new_j as usize;
        if 0 <= new_i && new_i < m as isize && 0 <= new_j && new_j < n as isize && grid[size_i][size_j] == '@' {
            adj += 1;
        }
    }
    adj < 4
}
