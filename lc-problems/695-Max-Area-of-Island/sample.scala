  object Solution {
    import scala.collection.mutable
    def maxAreaOfIsland(grid: Array[Array[Int]]): Int = {
      val visited: mutable.HashSet[(Int, Int)] = mutable.HashSet.empty[(Int, Int)]

      def computeArea(row: Int, column: Int): Int = {
        if (
          row < 0 ||
          row >= grid.length ||
          column < 0 ||
          column >= grid(row).length ||
          grid(row)(column) == 0 ||
          visited.contains((row, column))) {
          0
        }
        else {
          visited.add((row, column))
          1 + computeArea(row + 1, column) + computeArea(row - 1, column) + computeArea(row, column - 1) + computeArea(row, column + 1)
        }
      }

      val islandAreas: Seq[Int] = for {
        row <- grid.indices
        column <- grid(row).indices
        if grid(row)(column) == 1
        if !visited.contains((row, column))
      } yield computeArea(row, column)

      if (islandAreas.isEmpty) 0
      else islandAreas.max
    }
  }