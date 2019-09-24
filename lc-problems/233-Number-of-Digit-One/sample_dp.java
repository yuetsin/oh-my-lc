class Solution {
    public int countDigitOne(int n) {
        if (n <= 0) return 0;
        int[] digits = new int[10];        
        int pos = 0;
        while (n > 0) {
            digits[pos++] = n % 10;
            n /= 10;
        }
        return dfs(digits, pos - 1, new int[10][10], 0, true);
    }
    
    public int dfs(int[] digits, int pos, int[][] dp, int cnt, boolean limit) {
        if (pos == -1) return cnt;
        if (!limit && dp[pos][cnt] != 0) return dp[pos][cnt];
        int up = limit ? digits[pos] : 9;
        int ans = 0;
        for (int i = 0; i <= up; i++) {
            ans += dfs(digits, pos - 1, dp, cnt + (i == 1 ? 1 : 0), limit && i == up);
        }
        if (!limit) dp[pos][cnt] = ans;
        return ans;
    }
}