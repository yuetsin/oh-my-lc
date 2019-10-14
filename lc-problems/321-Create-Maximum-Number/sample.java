class Solution {
    //核心就是两个指针，依次对比，在满足canSkip情况下，找最大的值。难点是如果最大值相同，则需要迭代处理。
    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        //canSkip : 最多可以跳过多少个
        int canSkip = nums1.length - 0 + nums2.length - 0 - k;
        return helper(nums1, 0, nums2, 0, k, canSkip, 1).result;
    }
    //最后一个参数ifSameThenWhich表示两者皆可选的情况下，选择哪个1表示选第一个数组，2表示选第二个数组。
    public ResultInfo helper(int[] nums1, int start1, int[] nums2, int start2, int k, int canSkip, int ifSameThenWhich) {
        int[] result = new int[k];
        for (int index = 0; index < k; index++) {
            int max1Index = maxWithSkip(nums1, start1, canSkip);
            int max2Index = maxWithSkip(nums2, start2, canSkip);
            if (max1Index != -1 && max2Index != -1 && nums1[max1Index] > nums2[max2Index] || max1Index != -1 && max2Index == -1) {//第一个数组的大，选第一个数组
                result[index] = nums1[max1Index];
                canSkip = canSkip - (max1Index - start1);
                start1 = max1Index + 1;
            } else if (max1Index != -1 && max2Index != -1 && nums2[max2Index] > nums1[max1Index] || max2Index != -1 && max1Index == -1) {//第二个数组的大，选第二个数组
                result[index] = nums2[max2Index];
                canSkip = canSkip - (max2Index - start2);
                start2 = max2Index + 1;
            } else {//两值相等，则假设选1或选2后续值比较
                boolean done = false;
                int newK = k - index - 1;//还剩多少个没选
                int newStart1 = max1Index + 1;//假设选1则1新的start1为newStart1
                int canSkip1 = canSkip - (max1Index - start1);//假设选1则1新的canSkip为canSkip1
                int newStart2 = max2Index + 1;//假设选2则2新的start2为newStart2
                int canSkip2 = canSkip - (max2Index - start2);//假设选2则2新的canSkip为canSkip2
                ResultInfo resultInfo1 = new ResultInfo(null, newStart1, start2, canSkip1);
                ResultInfo resultInfo2 = new ResultInfo(null, start1, newStart2, canSkip2);
                for (int tmpK = 1; tmpK <= newK; tmpK++) {//注意优化：每次只计算长度为1的数组，如果相同，再计算后面的
                    //假设选1
                    resultInfo1 = helper(nums1, resultInfo1.start1, nums2, resultInfo1.start2, 1, resultInfo1.canSkip, 1);
                    int result1 = resultInfo1.result[0];
                    //假设选2
                    resultInfo2 = helper(nums1, resultInfo2.start1, nums2, resultInfo2.start2, 1, resultInfo2.canSkip, 2);
                    int result2 = resultInfo2.result[0];
                    if (result1 > result2) {
                        //选1
                        result[index] = nums1[max1Index];
                        canSkip = canSkip - (max1Index - start1);
                        start1 = max1Index + 1;
                        done = true;
                        break;
                    } else if (result1 < result2) {
                        //选2
                        result[index] = nums2[max2Index];
                        canSkip = canSkip - (max2Index - start2);
                        start2 = max2Index + 1;
                        done = true;
                        break;
                    }
                }
                if (!done) {//都行，根据ifSameThenWhich选
                    if (ifSameThenWhich == 1) {
                        result[index] = nums1[max1Index];
                        canSkip = canSkip - (max1Index - start1);
                        start1 = max1Index + 1;
                    } else {
                        result[index] = nums2[max2Index];
                        canSkip = canSkip - (max2Index - start2);
                        start2 = max2Index + 1;
                    }
                }
            }
        }
        return new ResultInfo(result, start1, start2, canSkip);
    }
    //在满足canSkip条件下，找最大值。
    public int maxWithSkip(int[] nums, int start, int canSkip) {//返回最大值下标
        if (start == nums.length) {
            return -1;
        }
        int index = start;
        for (int i = 1; i <= canSkip; i++) {
            if (start + i < nums.length && nums[start + i] > nums[index]) {
                index = start + i;
            }
        }
        return index;
    }
}
class ResultInfo {//结果和结束时的状态值，其中状态值用于迭代优化
    int[] result;
    int start1;
    int start2;
    int canSkip;

    public ResultInfo(int[] result, int start1, int start2, int canSkip) {
        this.result = result;
        this.start1 = start1;
        this.start2 = start2;
        this.canSkip = canSkip;
    }
}