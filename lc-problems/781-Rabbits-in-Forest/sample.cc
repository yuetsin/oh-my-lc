class Solution {
public:
    int numRabbits(vector<int>& answers)
    {
        unordered_map<int, int> mp;

        for (int i : answers) {
            if (!mp.count(i)) {
                mp[i] = 1;
            } else {
                mp[i]++;
            }
        }

        int d = 0;

        for (int i : answers) {
            if (mp[i] > 0) {
                d += ceil((double)mp[i] / (double)(i + 1)) * (i + 1) - mp[i];
                mp[i] = 0;
            }
        }

        return answers.size() + d;
    }
};