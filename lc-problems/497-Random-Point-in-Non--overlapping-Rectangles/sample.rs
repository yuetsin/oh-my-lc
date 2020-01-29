use rand::prelude::*;

#[derive(Debug)]
struct Solution {
    rects: Vec<Vec<i32>>,
    partial_sum: Vec<i32>,
    total: i32,
    rng: ThreadRng,

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {
    fn new(rects: Vec<Vec<i32>>) -> Self {
        let mut t = 0;
        let mut s = Vec::<i32>::new();
        for x in &rects {
            t += (x[2] - x[0] + 1) * (x[3] - x[1] + 1);
            s.push(t);
        }
        Solution {
            rects,
            partial_sum: s,
            total: t,
            rng: Default::default(),
        }
    }

    fn pick(&mut self) -> Vec<i32> {
        let targ = self.rng.gen_range(0, self.total);

        let mut lo = 0;
        let mut hi = self.rects.len() - 1;
        while lo != hi {
            let mid = (lo + hi) / 2;
            if targ >= *self.partial_sum.get(mid).unwrap() { lo = mid + 1; } else { hi = mid; }
        }
        let x = &self.rects[lo];
        let width = x[2] - x[0] + 1;
        let height = x[3] - x[1] + 1;
        let base = *self.partial_sum.get(lo).unwrap() - width * height;
        vec![x[0] + (targ - base) % width, x[1] + (targ - base) / width]
    }
}