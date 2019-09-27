def missingNumber(self, nums):
    return reduce(operator.xor, nums + range(len(nums)+1))
