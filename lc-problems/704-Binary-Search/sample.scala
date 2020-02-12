// written by @Java_Yan

import scala.annotation.tailrec

object Solution {
    def search(nums: Array[Int], target: Int): Int = {
        @tailrec
        def helper(left: Int, right: Int): Int = {
            val mid = left + (right - left) / 2
            if (left > right) -1
            else if (nums(mid) == target) mid
            else if (nums(mid) < target) helper(mid + 1, right)
            else helper(left, mid - 1)
        }
        helper(0, nums.length - 1)
    }
}