class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        min_offset = 100000
        rst = nums[0] + nums[1] + nums[2]
        zero_count = nums.count(0)

        nums.sort()
        numlen = len(nums)

        for i in range(numlen - 2):
            try:
                if nums[i] == nums[i - 1]:
                    continue
            except IndexError:
                pass
            l, r = i + 1, numlen - 1

            while l < r:
                offset = nums[i] + nums[l] + nums[r] - target
                if offset < 0:
                    if abs(offset) < min_offset:
                        rst = nums[i] + nums[l] + nums[r]
                        min_offset = abs(offset)
                    l += 1

                elif offset > 0:
                    if abs(offset) < min_offset:
                        rst = nums[i] + nums[l] + nums[r]
                        min_offset = abs(offset)
                    r -= 1

                else:
                    # rst_lst.append([nums[i], nums[l], nums[r]])
                    rst = nums[i] + nums[l] + nums[r]
                    min_offset = 0
                    break

        return rst
