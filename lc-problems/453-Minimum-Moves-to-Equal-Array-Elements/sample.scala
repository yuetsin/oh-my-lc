def minMoves(nums: Array[Int]): Int = {
  val min = nums reduceLeft (math.min(_, _))
  (nums foldLeft 0) (_ + _ - min)
}