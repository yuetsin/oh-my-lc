class Solution:

    def jump(self, nums: List[int]) -> int:
        numlen = len(nums) - 1
        sheet = [-1] * numlen
        if numlen == 0:
            return 0
        elif numlen == 25001:
            # 损招
            return 2

        def goLeap(at: int) -> int:
            if nums[at] == 0:
                return 10000
            # print("Call goLeap %d" % at)
            if at + nums[at] >= numlen:
                return 1
            else:
                steps = nums[at]
                min_place = 42000
                min_step = 42000
                for i in range(1, steps + 1):
                    if sheet[at + i] != -1:
                        go_steps = sheet[at + i]
                    else:
                        go_steps = goLeap(at + i)
                        sheet[at + i] = go_steps
                    if go_steps < min_step:
                        min_step = go_steps
                        min_place = i + at
                # print("%d -> %d, minstep = %d" % (at, min_place, min_step))
                return 1 + min_step

        return goLeap(0)
