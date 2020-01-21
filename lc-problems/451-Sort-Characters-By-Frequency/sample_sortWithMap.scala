import scala.collection.mutable

object Solution {
  def frequencySort(s: String): String = {
    if (s == null || s.length < 1) return s
	
    val map = mutable.Map[Char, Int]()
    for (c <- s) map.put(c, map.getOrElse(c, 0) + 1)

    map.toArray
      .sortWith((e1, e2) => e1._2 > e2._2) // order by cnt desc
      .map { case (c, cnt) => c.toString * cnt } // repeat char
      .mkString
  }
}