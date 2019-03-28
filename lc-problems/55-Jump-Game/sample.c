int Max(int a, int b) {
    return a > b ? a : b;
}
bool canJump(int* nums, int numsSize) {
    int max = 0, i = 0, goal = numsSize - 1;
    for (;; ++i) {
        max = Max(max, i + nums[i]);
        if (max >= goal)
            return true;
        if (max == i)
            return false;
    }
}