class Solution:

    def search(self, nums: List[int], target: int) -> int:

        if len(nums) < 3:
            try:
                return nums.index(target)
            except ValueError:
                return -1

        def binarySearch(nums: List[int], target: int) -> int:
            numlen = len(nums)
            if numlen == 1:
                return 0 if nums[0] == target else -1
            elif numlen == 2:
                    return nums.index(target)
                except ValueError:
                    return -1
            split_point = int(numlen / 2)
            if nums[split_point] == target:
                return split_point
            elif nums[split_point] < target:
                find = binarySearch(nums[split_point + 1:], target)
                return find + split_point + 1 if find != -1 else -1
            else:
                return binarySearch(nums[:split_point], target)

        def findCrackPlace(nums: List[int]) -> int:
            numlen = len(nums)
            if numlen == 1:
                return -1
            elif numlen == 2:
                return -1 if nums[0] < nums[1] else 1

            split_point = int(numlen / 2)
            crack1 = findCrackPlace(nums[:split_point])
            crack2 = findCrackPlace(nums[split_point:])
            if crack1 != -1:
                return crack1
            elif crack2 != -1:
                return crack2 + split_point
            else:
                return split_point if nums[split_point] < nums[split_point - 1] else -1

        crack_itm = findCrackPlace(nums)
        # print("crack at %d" % crack_itm)
        if crack_itm == -1:
            return binarySearch(nums, target)
        if nums[0] == target:
            return 0
        elif nums[0] > target:
            # print("bin in %s " % str(nums[crack_itm:]))
            result = binarySearch(nums[crack_itm:], target)
            return result + crack_itm if result != -1 else -1
        else:
            # print("bin in %s " % str(nums[:crack_itm]))
            return binarySearch(nums[:crack_itm], target)
