class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # return False
        final_step = len(nums) - 1

        def canOrNot(at: int) -> bool:
            max_steps = nums[at]

            if at + max_steps >= final_step:
                return True

            if max_steps == 0:
                return False

            for i in range(1, max_steps + 1):
                if canOrNot(at + i):
                    return True

            return False

        return canOrNot(0)
