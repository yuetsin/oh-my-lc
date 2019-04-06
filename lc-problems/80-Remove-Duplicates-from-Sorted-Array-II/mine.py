class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_count = len(nums)
        ptr = 0

        while ptr < num_count:
            if ptr > 1:
                if nums[ptr] == nums[ptr - 1] and nums[ptr - 1] == nums[ptr - 2]:
                    del nums[ptr]
                    num_count -= 1
                    continue
            ptr += 1

        return len(nums)
