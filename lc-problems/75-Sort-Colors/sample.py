def sortColors(self, nums):
    i = j = 0
    for k in xrange(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1

# 86 / 86 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# 84.03%

# @dietpepsi
