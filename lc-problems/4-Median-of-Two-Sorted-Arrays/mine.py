class Solution:

    def trivialMedian(self, nums: List[int]) -> float:
        if len(nums) % 2 == 1:
            return float(nums[int(len(nums) / 2)])
        else:
            return (nums[int(len(nums) / 2)] + nums[int(len(nums) / 2) - 1]) / 2.0

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            return self.trivialMedian(nums2)
        elif len(nums2) == 0:
            return self.trivialMedian(nums1)

        trig1 = 0
        trig2 = 0

        max_index1 = len(nums1)
        max_index2 = len(nums2)

        len_limit = (len(nums1) + len(nums2)) / 2
        tail = (len(nums1) + len(nums2)) % 2

        count = 0
        new_list = []
        while count <= len_limit:
            if trig1 == max_index1:
                new_list.append(nums2[trig2])
                trig2 += 1
            elif trig2 == max_index2:
                new_list.append(nums1[trig1])
                trig1 += 1
            elif nums1[trig1] > nums2[trig2]:
                new_list.append(nums2[trig2])
                trig2 += 1
            else:
                new_list.append(nums1[trig1])
                trig1 += 1
            count += 1
        # return new_list
        if tail == 1:
            return new_list[-1]
        else:
            return (new_list[-1] + new_list[-2]) / 2
