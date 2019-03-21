class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                del nums[idx]

                # print("idx = %d" % idx)
                # print("cnt = %d" % cnt)
                # print("lst = %s" % nums)
            else:
                idx += 1
                cnt += 1
                # print("idx = %d" % idx)
                # print("lst = %s" % nums)
        # print("cnt = %d" % cnt)
        return cnt
