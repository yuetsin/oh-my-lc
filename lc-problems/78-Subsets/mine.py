class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rst = []
        if nums == []:
            return [[]]
        else:
            for i in [0]:
                this = nums[i]
                del nums[i]
                lists = self.subsets(nums)
                nums.insert(i, this)
                for itm in lists:
                    itm.sort()
                    rst.append(itm)
                    rst.append([this] + itm)
        return rst