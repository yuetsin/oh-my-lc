class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subsets(nums: List[int]) -> List[List[int]]:
            rst = []
            if nums == []:
                return [[]]
            else:
                for i in [0]:
                    this = nums[i]
                    del nums[i]
                    lists = subsets(nums)
                    nums.insert(i, this)
                    for itm in lists:
                        itm.sort()
                        rst.append(itm)
                        rst.append([this] + itm)
            return rst
        subset_idxs = subsets(list(range(len(nums))))
        rst_sets = []
        for itm in subset_idxs:
            for k in range(len(itm)):
                itm[k] = nums[itm[k]]
            itm.sort()
            if not itm in rst_sets:
                rst_sets.append(itm)
        return rst_sets
