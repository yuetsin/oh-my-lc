object Solution {
  def frequencySort(s: String): String = {
    import collection.mutable.Map
    val count: Map[Char, Int] = Map().withDefaultValue(0)
    for {
      c <- s
    } {
      count(c) += 1
    }
    count
      .toList.map(x => (x._2, x._1))
      .sorted
      .reverse
      .flatMap(x => List.fill(x._1)(x._2.toString))
      .foldLeft("")(_ + _)
  }
}