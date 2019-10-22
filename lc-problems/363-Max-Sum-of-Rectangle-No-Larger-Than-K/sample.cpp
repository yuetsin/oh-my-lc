class Solution {
public:
    void print(vector<int>& v) {
        for (auto i : v) {
            cout << i << ",";
        }
        cout << endl;
    }
    
    int maxSum(vector<int>& rangesum, int l, int r, int k) {
        if (l > r) return -1;
        if (l == r) return rangesum[r+1] - rangesum[l] <= k ? rangesum[r+1] - rangesum[l] : -0x7fffffff;
        int m = (l + r) / 2;
        //cout << "l:" << l << " r:" << r << endl;
        vector<int> range(rangesum.begin() + l, rangesum.begin() + r+2);
        
        for (int i = 0; i <= m - l; i++) range[i] = -range[i];
        sort(range.begin(), range.begin() + m - l + 1);
        sort(range.begin() + m - l + 1, range.end());
        //print(range);
        int s = 0;
        int ret = -0x7fffffff;
        for (int e = r - l + 1; e > m - l; e--) {
            while (s <= m - l and range[s] + range[e] <= k) {
                ret = max(ret, range[s] + range[e]);
                s += 1;
            }
        }
        ret = max(ret, maxSum(rangesum, l, m, k));
        ret = max(ret, maxSum(rangesum, m+1, r, k));
        return ret;
    }
    
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        vector<vector<int>> presum;
        int R = matrix.size();
        int C = matrix[0].size();
        if (R > C) {
            vector<vector<int>> new_matrix;
            for (int j = 0; j < C; j++) {
                new_matrix.push_back(vector<int>());
                for (int i = 0; i < R; i++) {
                    new_matrix[j].push_back(matrix[i][j]);
                }
            }
            matrix.clear();
            for (int j = 0; j < C; j++) {
                matrix.push_back(new_matrix[j]);
            }
            R = matrix.size();
            C = matrix[0].size();
        }
        
        for (int i = 0; i < R; i++) {
            presum.push_back(vector<int>());
            presum[i].push_back(0);
            for (int j = 0; j < C; j++)
                presum[i].push_back(presum[i][j] + matrix[i][j]);
        }
        int ret = -0x7fffffff;
        for (int i = 0; i < R; i++) {
            vector<int> rangesum;
            for (int j = 0; j <= C; j++) rangesum.push_back(0);
            for (int height = 1; height + i - 1 < R; height++) {
                for (int j = 0; j < C; j++) rangesum[j+1] += presum[i+height-1][j+1];
                ret = max(ret, maxSum(rangesum, 0, C-1, k));
            }
        }
        return ret <= -0x7fffffff ? -1 : ret;
    }
};