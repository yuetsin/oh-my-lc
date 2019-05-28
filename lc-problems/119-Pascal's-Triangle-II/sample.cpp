class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if (rowIndex < 0)
            return vector<int>();
        else if (rowIndex == 0)
            return vector<int>({ 1 });

        vector<int> prevRow({ 1, 1 });
        if (rowIndex == 1)
            return prevRow;

        int startId = 2;
        while (startId <= rowIndex) {
            vector<int> row(1 + (startId++), 1);
            for (int j = 1; j < row.size() - 1; j++)
                row[j] = prevRow[j] + prevRow[j - 1];
            prevRow = row;
        }

        return prevRow;
    }
};