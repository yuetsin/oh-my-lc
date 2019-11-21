impl Solution {
    pub fn find_nth_digit(n: i32) -> i32 {
        let mut n:     u64 = n as u64;
        let mut count: u64 = 9;
        let mut power: u64 = 1;
        let mut level: u64 = 1;

        while n > count {
            n -= count;
            level += 1;
            power *= 10;
            count = 9 * level * power;
        }

        n -= 1;
        let j = (level - 1) - n % level;
        n = power + n / level;
        
        for _ in 0..j {
            n /= 10
        }
        
        (n % 10) as i32
    }
}