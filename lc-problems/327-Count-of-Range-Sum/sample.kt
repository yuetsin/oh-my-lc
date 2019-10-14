class Solution {
    var count = 0

    fun countRangeSum(nums: IntArray, lower: Int, upper: Int): Int {
        val m = nums.size
        val sum = LongArray(m + 1)
        for (i in 1..m) {
            sum[i] = sum[i - 1] + nums[i - 1]
        }
        mergeSort(sum, 0, m, lower, upper)
        return count
    }

    private fun mergeSort(sum: LongArray, start: Int, end: Int, lower: Int, upper: Int) {
        if (start >= end) {
            return
        }
        val mid = start + (end - start)/2
        mergeSort(sum, start, mid, lower, upper)
        mergeSort(sum, mid + 1, end, lower, upper)
        var l = start
        var r = mid + 1
        var R = mid + 1
        while (l <= mid) {
            while (r <= end && sum[r] < sum[l] + lower) {
                r++
            }
            if (r == end + 1) break
            while (R <= end && sum[R] <= upper + sum[l]) {
                R++
            }
            count += R - r
            l++
        }
        l = start
        r = mid + 1
        val array = LongArray(end - start + 1)
        var idx = 0
        while (l <= mid && r <= end) {
            if (sum[l] <= sum[r]) {
                array[idx++] = sum[l++];
            } else {
                array[idx++] = sum[r++];
            }
        }
        while (l <= mid) {
            array[idx++] = sum[l++];
        }
        while (r <= end) {
            array[idx++] = sum[r++];
        }
        for (i in start..end) {
            sum[i] = array[i - start]
        }
    }
}