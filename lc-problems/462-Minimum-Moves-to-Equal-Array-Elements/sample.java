#!/usr/bin/env python

    public int minMoves2(int[] nums) {
        int ret = 0;
        Arrays.sort(nums);
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            ret += nums[right] - nums[left];
            left++;
            right--;
        }   
        return ret;
    }  