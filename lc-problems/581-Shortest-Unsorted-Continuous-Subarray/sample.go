// written by @tjucoder

func findUnsortedSubarray(nums []int) int {
    sorted := make([]int, len(nums))
    copy(sorted, nums)
    sort.Ints(nums)
    l, r := 0, -1
    for i := 0; i < len(nums); i++ {
        if sorted[i] != nums[i] {
            l = i
            break
        }
    }
    for i := len(nums)-1; i >= 0; i-- {
        if sorted[i] != nums[i] {
            r = i
            break
        }
    }
    return r-l+1
}