typealias GridIndex = (row: Int, col: Int)

class Node {
    var val: Int = 0
    var isLeaf: Bool
    var topLeft: Node?
    var topRight: Node?
    var bottomLeft: Node?
    var bottomRight: Node?
    
    init(val: Int, isLeaf: Bool, topLeft: Node?, topRight: Node?, botLeft: Node?, botRight: Node?) {
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = botLeft
        self.bottomRight = botRight
    }
}

func constructQuadTree( _ grid: inout [[Int]], _ length: Int, topLeft: GridIndex, botRight: GridIndex) -> Node?
{
    guard isPowerOfTwo(length) else {
        return nil
    }
    
    if length == 1 {
        return Node(val: grid[topLeft.row][topLeft.col], isLeaf: true, topLeft: nil, topRight: nil, botLeft: nil, botRight: nil)
    }
    
    let newLength = length / 2
    let bottomRightPoint: GridIndex = (topLeft.row + newLength, topLeft.col + newLength)
    
    // For Top Left Quadrant
    let topLeftNode = constructQuadTree(&grid, newLength, topLeft: topLeft, botRight: (bottomRightPoint.row - 1, bottomRightPoint.col - 1))
    
    // For Top Right Quadrant
    let topRightNode = constructQuadTree(&grid, newLength, topLeft: (row: topLeft.row, col: bottomRightPoint.col), botRight: (bottomRightPoint.row - 1, botRight.col))
    
    // For Bot Left Quadrant
    let botLeftNode = constructQuadTree(&grid, newLength, topLeft: (row: bottomRightPoint.row, col: topLeft.col), botRight: (botRight.row, bottomRightPoint.col - 1))
    
    // For Bot Right Quadrant
    let botRightNode = constructQuadTree(&grid, newLength, topLeft: bottomRightPoint, botRight: botRight)
    
    // If all nodes are leaves and all leaves have same value then we can construct this as a leaf
    if let topLeftNode = topLeftNode, let topRightNode = topRightNode, let botLeftNode = botLeftNode, let botRightNode = botRightNode, topLeftNode.isLeaf, topRightNode.isLeaf, botLeftNode.isLeaf, botRightNode.isLeaf {
        
        let compareValue = (topLeftNode.val + botRightNode.val + botLeftNode.val + topRightNode.val)
        
        // The values must be the same
        if compareValue == 4 || compareValue == 0 {
            return Node(val: topLeftNode.val, isLeaf: true, topLeft: nil, topRight: nil, botLeft: nil, botRight: nil)
        }
    }
    
    return Node(val: -1, isLeaf: false, topLeft: topLeftNode, topRight: topRightNode, botLeft: botLeftNode, botRight: botRightNode)
}

func isPowerOfTwo(_ x: Int) -> Bool {
    return (x & (x - 1)) == 0 && x != 0
}