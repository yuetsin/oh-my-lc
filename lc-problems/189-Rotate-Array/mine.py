class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums) - k
        nlst = nums[k:] + nums[:k]
        for i in range(len(nums)):
            nums[i] = nlst[i]
