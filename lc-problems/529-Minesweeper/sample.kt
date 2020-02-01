class Minesweeper {
    data class Point(val row: Int, val col: Int)

    private val adjacent = listOf(
        Point(-1, -1),
        Point(-1, 0),
        Point(-1, 1),
        Point(0, -1),
        Point(0, 1),
        Point(1, -1),
        Point(1, 0),
        Point(1, 1)
    )

    fun updateBoard(board: Array<CharArray>, click: IntArray) =
        board.apply {
            val (row, col) = click
            when (this[row][col]) {
                'M' -> this[row][col] = 'X'
                else -> reveal(this, Point(row, col))
            }
        }

    private fun reveal(board: Array<CharArray>, p: Point) {
        fun isInBound(p: Point) = (p.row in board.indices && p.col in board[0].indices)

        fun isBomb(p: Point) = board[p.row][p.col] == 'M'

        fun adjacentSquares(p: Point) = adjacent.map {
            Point(p.row + it.row, p.col + it.col)
        }

        if (!isInBound(p) || board[p.row][p.col] != 'E')
            return

        adjacentSquares(p)
            .filter { isInBound(it) }
            .count { isBomb(it) }
            .let { n ->
                if (n > 0) {
                    board[p.row][p.col] = '0'.plus(n)
                    return
                }
                
                board[p.row][p.col] = 'B'
                adjacentSquares(p).forEach { reveal(board, it) }
            }
    }
}
