class Solution {
    func convert(_ s: String, _ numRows: Int) -> String {
        guard numRows > 1 else {return s}
        var charBack = [Character]()
        let chars = Array(s)
        for i in 0..<numRows {
            var p = i
            if p < chars.count {
                charBack.append(chars[p])
            }

            let fullDistance = 2 * (numRows - 1)
            let del = 2 * p != fullDistance ? 2 * p : 0
            var distance = del > 0 ? fullDistance - del : fullDistance

            p += distance
            while p < chars.count {
                charBack.append(chars[p])
                distance = del > 0 ? fullDistance - distance : fullDistance
                p += distance
            }
        }
        return String(charBack)
    }
}