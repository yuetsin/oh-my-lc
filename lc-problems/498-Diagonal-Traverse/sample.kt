fun findDiagonalOrder(matrix: Array<IntArray>): IntArray {

    if (matrix.isEmpty()) return intArrayOf()

    var row = 0
    var col = 0

    var maxRow = matrix.size - 1
    val maxCol = matrix[0].size - 1

    var results = mutableListOf<Int>()
    var directionDown = false

    while (true) {
        results.add(matrix[row][col])

        if (row == maxRow && col == maxCol) {
            return results.toIntArray()
        }

        if (!directionDown) {
            // moving up right
            if (row == 0) {
                // top wall, reverse
                // if not at right well move right, else move down
                if (col < maxCol) {
                    col++
                } else {
                    row++
                }

                directionDown = true
            } else if (col == maxCol) {
                // right wall, reverse
                row++
                directionDown = true
            } else {
                row--
                col++
            }

        } else {
            // moving down left
            if (col == 0) {
                // left wall
                if (row < maxRow) {
                    row++
                } else {
                    col++
                }
                directionDown = false
            } else if (row == maxRow) {
                // bottom wall
                col = Math.min(maxCol, col + 1)
                directionDown = false
            } else {
                // move down left
                row++
                col--
            }
        }
    }
}