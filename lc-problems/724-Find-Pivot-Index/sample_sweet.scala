def pivotIndex(nums: Array[Int]): Int = {
  def pivotAcc(i: Int, leftSum: Int, rightSum: Int): Int = 
    if (i == nums.length) -1
    else if (leftSum == rightSum - nums(i)) i
    else pivotAcc(i + 1, leftSum + nums(i), rightSum - nums(i))

  pivotAcc(0, 0, nums.sum)
}