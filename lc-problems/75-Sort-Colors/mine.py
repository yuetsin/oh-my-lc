class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        green = 0
        blue = 0
        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                green += 1
            elif i == 2:
                blue += 1

        idx = 0
        for _ in range(red):
            nums[idx] = 0
            idx += 1

        for _ in range(green):
            nums[idx] = 1
            idx += 1

        for _ in range(blue):
            nums[idx] = 2
            idx += 1
