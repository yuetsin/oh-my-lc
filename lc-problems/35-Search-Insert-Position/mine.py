class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        def binSearch(nums: List[int], target: int) -> int:
            # print("= = = called = = =")
            
            numcnt = len(nums)
            if numcnt < 3:
                try:
                    return nums.index(target)
                except:
                    if numcnt == 2:
                        return 1 if (nums[0] < target and target < nums[1]) else -1
                    return -1

            breakPoint = int(len(nums) / 2)
            # print("brkPnt = %d" % breakPoint)
            rst1 = binSearch(nums[:breakPoint], target)
            rst2 = binSearch(nums[breakPoint:], target)
            # print("rst1 = %d, rst2 = %d" % (rst1, rst2))
            if rst1 != -1:
                return rst1
            elif rst2 != -1:
                return rst2 + breakPoint
            else:
                return breakPoint if (nums[breakPoint - 1] < target and nums[breakPoint] > target) else -1
        return binSearch(nums, target)

