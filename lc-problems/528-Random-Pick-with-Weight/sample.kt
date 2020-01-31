import java.util.*
import kotlin.random.Random

class Solution(w: IntArray) {
    private val indexes = TreeMap<Int, Int>()
    private var sum = 0

    init {
        for (i in 0 until w.size) {
            sum += w[i]
            indexes[sum] = i
        }
    }

    fun pickIndex(): Int {
        val index = Random.nextInt(1, sum + 1)
        return indexes.ceilingEntry(index).value
    }
}