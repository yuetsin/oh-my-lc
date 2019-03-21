class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        rst_lst = []

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
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1

                elif sum > 0:
                    r -= 1

                else:
                    rst_lst.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    try:
                        while nums[l - 1] == nums[l]:
                            l += 1
                        while nums[r] == nums[r + 1]:
                            r -= 1
                    except IndexError:
                        pass

        if zero_count > 2:
            if not [0, 0, 0] in rst_lst:
                rst_lst.append([0, 0, 0])
        return rst_lst
