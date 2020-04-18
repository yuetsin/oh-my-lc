// written by @haitao1996

class Solution {
public:
    int swimInWater(vector<vector>& grid)
    {
        int n = grid.size();
        int l = grid[0][0], r = n * n - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            vector<vector> map(n, vector(n, 0));
            find(grid, mid, 0, 0, map);
            if (map[n - 1][n - 1] == 1)
                r = mid;
            else
                l = mid + 1;
        }
        return l;
    }
    void find(vector<vector>& grid, int mid, int x, int y, vector<vector>& map)
    {
        if (x < 0 || x >= grid.size() || y < 0 || y >= grid.size() || grid[x][y] > mid)
            return;
        if (map[x][y] == 0)
            map[x][y] = 1;
        else
            return;
        find(grid, mid, x - 1, y, map);
        find(grid, mid, x + 1, y, map);
        find(grid, mid, x, y - 1, map);
        find(grid, mid, x, y + 1, map);
    }
};