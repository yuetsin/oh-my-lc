class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_num = None
        cnt = 0
        ptr = 0
        while ptr < len(nums):
            if last_num != nums[ptr]:
                last_num = nums[ptr]
                cnt += 1
                ptr += 1
            else:
                del nums[ptr]

        return cnt
