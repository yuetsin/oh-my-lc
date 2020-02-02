class Solution {
    fun checkRecord(s: String): Boolean {
        var p = 0
        var a = 0
        while (p < s.length) {
            var q = p + 1
            while (q < s.length && s[q] == s[p]) {
                q++
            }
            if (s[p] == 'A') a += q - p
            if (s[p] == 'L' && q - p > 2) return false
            p = q
        }
        return a <= 1
    }
}