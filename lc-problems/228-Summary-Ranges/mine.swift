class Solution {
    func summaryRanges(_ array: [Int]) -> [String] {
        if array.count == 0 {
            return []
        } else if array.count == 1 {
            return ["\(array.first!)"]
        }
        var begin = array.first!
        var last = array.first!

        var resultPair: [String] = []
        
        var firstSkip = true
        for integer in array {
            if firstSkip {
                firstSkip = false
                continue
            }
            if integer - last == 1 {
                last += 1
            } else {
                if begin != last {
                    resultPair.append("\(begin)->\(last)")
                } else {
                    resultPair.append("\(begin)")
                }
                begin = integer
                last = integer
            }
        }
        if begin != last {
            resultPair.append("\(begin)->\(last)")
        } else {
            resultPair.append("\(begin)")
        }
        return resultPair
    }
}