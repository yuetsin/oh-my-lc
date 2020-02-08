#!/usr/bin/env python


def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    right = self.find_upper_closest(arr, x)
    left = right - 1

    for _ in range(k):
        if left < 0 or right > len(arr) - 1:
            break
        if arr[right] - x < x - arr[left]:
            right += 1
        else:
            left -= 1

    if left < 0:
        return arr[0:k]
    elif right > len(arr) - 1:
        return arr[-k:]
    else:
        return arr[right - k:right]


def find_upper_closest(self, arr, x):
    start, end = 0, len(arr) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if arr[mid] >= x:
            end = mid
        else:
            start = mid
    if arr[start] >= x:
        return start
    if arr[end] >= x:
        return end

    return len(arr)
