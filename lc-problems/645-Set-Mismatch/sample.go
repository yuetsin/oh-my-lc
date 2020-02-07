func findErrorNums(nums []int) []int {
	for i := 0; i < len(nums); i++ {
		for ; nums[i] != nums[nums[i]-1]; nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i] {}
	}
	for i, num := range nums {
		if num != i+1 {
			return []int{num, i + 1}
		}
	}
	return nil
}