class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums: List[int], target: int) -> int:
            numcnt = len(nums)
            if numcnt < 3:
                try:
                    return nums.index(target)
                except:
                    return -1
            breakPoint = int(len(nums) / 2)
            rst1 = binarySearch(nums[:breakPoint], target)
            rst2 = binarySearch(nums[breakPoint:], target)
            if rst1 != -1:
                return rst1
            elif rst2 != -1:
                return rst2 + breakPoint
            else:
                return -1
        found = binarySearch(nums, target)
        if found == -1:
            return [-1, -1]
        first = found
        last = found
        limit = len(nums) - 1
        
        while first > 0 and nums[first - 1] == target:
            first -= 1


        while last < limit and nums[last + 1] == target:
            last += 1
            
        return [first, last]