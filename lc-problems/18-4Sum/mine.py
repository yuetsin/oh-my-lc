class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        numlen = len(nums)

        p1 = 0
        p2 = 1
        p3 = numlen - 2
        p4 = numlen - 1

        possible_rst = []

        for p1 in range(0, numlen - 3):
            for p4 in range(p1 + 3, numlen):
                p2 = p1 + 1
                p3 = p4 - 1
                while p2 < p3:
                    sum = nums[p1] + nums[p2] + nums[p3] + nums[p4]
                    if sum > target:
                        p3 -= 1
                        try:
                            while nums[p3] == nums[p3 + 1]:
                                p3 -= 1
                        except:
                            pass
                    elif sum < target:
                        p2 += 1
                        try:
                            while nums[p2] == nums[p2 - 1]:
                                p2 += 1
                        except:
                            pass
                    else:
                        rst_piece = [nums[p1], nums[p2], nums[p3], nums[p4]]
                        if not rst_piece in possible_rst:
                            possible_rst.append(rst_piece)
                        p3 -= 1
                        try:
                            while nums[p3] == nums[p3 + 1]:
                                p3 -= 1
                        except:
                            pass
                        p2 += 1
                        try:
                            while nums[p2] == nums[p2 - 1]:
                                p2 += 1
                        except:
                            pass

        return possible_rst
