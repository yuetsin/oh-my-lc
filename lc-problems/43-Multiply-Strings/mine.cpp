#include <iostream>
#include <string>
#include <vector>
using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;
int main() {
    string numberOne, numberTwo;
    int numOneLen, numTwoLen;
    vector<int> resultNum;
    cout << "Please input the number 1: " << endl;
    cin >> numberOne;

    cout << "Please input the number 2: " << endl;
    cin >> numberTwo;

    // 确定确实读入了数据
    if (!(numOneLen = numberOne.length()) ||
        !(numTwoLen = numberTwo.length())) {
        return -1;
    }

    for (size_t i = 0; i < numOneLen + numTwoLen - 1; ++i) {
        resultNum.push_back(0);
    }
    // cout << numOneLen << numTwoLen;
    for (int i = 0; i < numOneLen; ++i) {
        int m = static_cast<int>(numberOne[numOneLen - i - 1]) - 48;
        for (int j = 0; j < numTwoLen; ++j) {
            int n = static_cast<int>(numberTwo[numTwoLen - j - 1]) - 48;
            resultNum[i + j] += m * n;
            /*
                ----debug----
                cout << i << endl;
                cout << j << endl;
                cout << m << endl;
                cout << n << endl;
             */
        }
    }
    /*
        for (auto i : resultNum) {
            cout << i << endl;
        }
     */
    for (size_t i = 0; i < numOneLen + numTwoLen - 2; ++i) {
        resultNum[i + 1] += resultNum[i] / 10;
        resultNum[i] %= 10;
        // cout << i + 1 << "位进了" << resultNum[i] / 10 << endl;
    }
    for (size_t i = 0; i < numOneLen + numTwoLen - 1; ++i) {
        cout << resultNum[numOneLen + numTwoLen - i - 2];
    }
}
