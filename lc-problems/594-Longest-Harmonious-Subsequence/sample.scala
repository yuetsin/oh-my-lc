// written by @alexeysurovtsev

import scala.collection.mutable._

object Solution {
  def findLHS(nums: Array[Int]): Int = {
    var m = HashMap[Int,Int]()

    nums.foreach(t=> m(t) = m.getOrElse(t,0)+1 )

    if(m.size == 0 || m.size == 1 ) return 0

    val it = m.toList.sortBy(t=>t._1).sliding(2).toList
    val it2 = it.filter(f=> Math.abs(f.head._1 - f.tail.head._1) == 1 )
    val it3 = it2.map(t=>t.head._2 + t.tail.head._2).toList

    if(it3.size == 0) return 0
    else return it3.max
  }
}