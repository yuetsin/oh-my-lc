class Solution {
public:
    int threeSumClosest(vector<int>& num, int target) {
        int clostAbs = INT_MAX;
        int clostSum = num[0] + num[1] + num[2];
        int low;
        int high;
        int sum = 0;
        sort(num.begin(), num.end());
        for (int i = 0; i < num.size() - 2; i++) {
            low  = i + 1;
            high = num.size() - 1;
            while (low < high) {
                sum = num[low] + num[high];
                if (abs(sum + num[i] - target) < clostAbs) {
                    clostAbs = abs(sum + num[i] - target);
                    clostSum = sum + num[i];
                }

                if (sum > (target - num[i])) {
                    high--;
                }
                else {
                    low++;
                }
            }
        }
        return clostSum;
    }
};