func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	totalLength := len(nums1) + len(nums2)
	if totalLength == 0 {
		return 0.0
	}

	if totalLength%2 == 1 {
		return findKthElement(nums1, nums2, 0, 0, (totalLength+1)/2)
	} else {
		return (findKthElement(nums1, nums2, 0, 0, totalLength/2) + findKthElement(nums1, nums2, 0, 0, totalLength/2+1)) / 2.0
	}
}

func findKthElement(nums1 []int, nums2 []int, s1 int, s2 int, k int) float64 {
	len1 := len(nums1) - s1
	len2 := len(nums2) - s2
	if len1 > len2 {
		return findKthElement(nums2, nums1, s2, s1, k)
	}

	if len1 == 0 {
		return float64(nums2[k-1])
	}

	if k == 1 {
		return float64(min(nums1[s1], nums2[s2]))
	}

	i1 := min(k/2, len1)
	i2 := k - i1

	if nums1[s1+i1-1] == nums2[s2+i2-1] {
		return float64(nums1[s1+i1-1])
	} else if nums1[s1+i1-1] < nums2[s2+i2-1] {
		return findKthElement(nums1, nums2, s1+i1, s2, k-i1)
	} else {
		return findKthElement(nums1, nums2, s1, s2+i2, k-i2)
	}
}

func min(a int, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}
