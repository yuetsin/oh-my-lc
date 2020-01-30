class Solution {
    fun fib(N: Int): Int {
        tailrec fun fib_(x: Int, y: Int, num: Int) : Int{
            return when(num){
                0 -> 0
                1 -> 1
                2 -> x + y
                else -> fib_(y, x + y, num - 1)
            }
        }
        return fib_(0, 1, N)
    }
}