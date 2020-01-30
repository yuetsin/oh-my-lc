class Solution {
    fun checkPerfectNumber(num: Int): Boolean {
        if(num <= 1) return false
        var lastLookUp = Int.MAX_VALUE
        var sum = 1
        for (i in 2 until num) {
            if(i >= lastLookUp) break
            if (num % i == 0) {
                sum += i + num/i
                lastLookUp = num/i
            }
        }
        return sum == num
    }
}