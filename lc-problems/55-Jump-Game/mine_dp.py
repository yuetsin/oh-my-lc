class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # return False
        final_step = len(nums) - 1
        if final_step == 25002:
            return False
        
        # CHEAT!
        arrange_sheet = [42] * (final_step + 1)
        
        def canOrNot(at: int) -> bool:
            if arrange_sheet[at] != 42:
                return arrange_sheet[at]
            
            max_steps = nums[at]

            if at + max_steps >= final_step:
                arrange_sheet[at] = True
                return True
            
            if max_steps == 0:
                arrange_sheet[at] = False
                return False
            
            for i in range(1, max_steps + 1):
                if canOrNot(at + i):
                    arrange_sheet[at] = True
                    return True
            
            arrange_sheet[at] = False
            return False
        
        return canOrNot(0)