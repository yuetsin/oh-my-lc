// written by @alptekin35

class KthLargest {

    var heap: Heap<Int> = Heap { (first, second) -> Bool in
        return first < second
    }

    var k: Int = -1
    
    init(_ k: Int, _ nums: [Int]) {
        self.k = k
        for item in nums {
            _ = add(item)
        }
    }
    
    func add(_ val: Int) -> Int {
        heap.insert(val)
        if heap.count > k {
            heap.remove()
        }
        return heap.peek()!
    }
}