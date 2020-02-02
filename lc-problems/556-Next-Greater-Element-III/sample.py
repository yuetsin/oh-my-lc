class Solution:
    def nextGreaterElement(self, n: int) -> int:
        index, arr = -1, [i for i in str(n)][::-1]
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                index = i
                break
        if index == -1:
            return -1
        j = bisect.bisect_right(arr, arr[index + 1], lo=0, hi=index + 1)
        arr[index+1], arr[j] = arr[j], arr[index+1]
        ret = int(''.join(arr[:index+1][::-1] + arr[index+1:])[::-1])
        return ret if ret < ((2 << 30) - 1) else -1
