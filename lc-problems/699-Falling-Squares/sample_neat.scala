def fallingSquares(positions: Array[Array[Int]]): List[Int] = {
        positions.scanLeft(List[(Int, Int, Int)]()) {
            case (interval, Array(s,h)) => 
                interval.filter(i => !(i._2 <= s || s + h <= i._1)) match { // 寻找交集
                    case List() => (s, s+h, h) +: interval
                    case ints => (s, s+h, h+ints.maxBy(_._3)._3) +: interval
                }       
        }.tail.map(_.maxBy(_._3)._3).toList
}