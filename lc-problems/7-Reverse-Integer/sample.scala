object Solution {
    def reverse(x: Int): Int = {
        val l  = Stream.iterate(x)(_ / 10).takeWhile(_ != 0).map(_%10)
        val r = l.foldLeft(0L) ((r,d) => r * 10 + d)
        if (r > Integer.MAX_VALUE || r < Integer.MIN_VALUE) 0
        else r.toInt
    }
}