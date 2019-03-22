class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        numcnt = len(nums) - 1
        ptr = numcnt - 1
        while ptr >= 0:
            if nums[ptr + 1] > nums[ptr]:
                break
            ptr -= 1

        key = nums[ptr]

        # print(ptr)
        if ptr == -1:
            nums.reverse()
            return

        lp = ptr + 1
        rp = numcnt
        while lp < rp:
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp += 1
            rp -= 1

        for i in range(ptr + 1, numcnt + 1):
            if nums[i] > key:
                nums[ptr], nums[i] = nums[i], nums[ptr]
                return
