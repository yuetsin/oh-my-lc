use std::collections::HashMap;
impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut comps = HashMap::new();
        comps.insert('}', '{');
        comps.insert(']', '[');
        comps.insert(')', '(');
        let mut stack = Vec::new();
        for ch in s.chars() {
            if ch == '(' || ch == '[' || ch == '{' {
                stack.push(ch);
            } else if (ch == ')' || ch == ']' || ch == '}') {
                if stack.is_empty() { return false; }
                let comp = stack.pop().unwrap();
                if comp != *comps.get(&ch).unwrap() { return false; }
            }
        }
        return stack.is_empty();
    }
}