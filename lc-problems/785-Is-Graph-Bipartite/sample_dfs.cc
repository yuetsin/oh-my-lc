class Solution
{
public:
    bool dfscolor(vector<vector> &adj, int n, int idx, bool *visited, int *color, int c)
    {
        visited[idx] = true;
        color[idx] = c;

        int e = adj[idx].size();
        //if(e==0)return false;
        for (int i = 0; i < e; i++)
        {
            int node = adj[idx][i];
            if (!visited[node])
            {
                if (!dfscolor(adj, n, node, visited, color, (c + 1) % 2))
                    return false;
            }
            else
            {
                if (color[node] == color[idx])
                {
                    return false;
                }
            }
        }
        return true;
    }
    bool isBipartite(vector<vector<int>> &adj)
    {

        int n = adj.size();

        bool *visited = new bool[n]();
        int *color = new int[n];
        for (int i = 0; i < n; i++)
            color[i] = -1;

        bool a = dfscolor(adj, n, 0, visited, color, 0);

        if (!a)
            return false;

        for (int i = 1; i < n; i++)
        {
            if (!visited[i])
            {
                bool b = dfscolor(adj, n, i, visited, color, 1);
                if (!b)
                    return false;
            }
        }
        return true;
    }
};