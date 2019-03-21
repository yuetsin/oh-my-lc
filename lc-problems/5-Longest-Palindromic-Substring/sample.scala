def longestPalindrome(s: String): String = {
    if (s == null) ""
    else {
      def findMaxPalindromeWithSetOrigin(s1: String, left: Int, right: Int): Int = {
        if (left < 0 || right >= s1.length || s1(left) != s1(right)) 0
        else 1 + findMaxPalindromeWithSetOrigin(s1, left - 1, right + 1)
      }
      
      var maxString = ""
      (0 until s.length).foreach { i =>
        val lengthWithOdd = findMaxPalindromeWithSetOrigin(s, i, i)
        if (lengthWithOdd * 2 - 1 > maxString.length) {
          maxString = s.substring(i - lengthWithOdd + 1, i + lengthWithOdd)
        }
        val lengthWithEven = findMaxPalindromeWithSetOrigin(s, i, i + 1)
        if (lengthWithEven * 2 > maxString.length) {
          maxString = s.substring(i - lengthWithEven + 1, i + lengthWithEven + 1)
        }
      }
      maxString
    }
  }