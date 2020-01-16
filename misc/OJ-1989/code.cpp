#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
using std::cin;
using std::cout;
using std::endl;
using std::vector;
vector<int> generateTriangle(int size, int amount) {
    vector<int> resultVec;
    for (size_t i = 0; i < size; i++) {
        resultVec.push_back(amount * i * 1.0 / size);
    }
    return resultVec;
}

vector<int> generateSquare(int size, int amount) {
    vector<int> resultVec;
    for (size_t i = 0; i < size; i++) {
        resultVec.push_back(amount);
    }
    return resultVec;
}
vector<int> generateCircle(int size, int amount) {
    vector<int> resultVec;
    for (size_t i = 0; i < size; i++) {
        resultVec.push_back(amount * sqrt(1 - pow((1 - i * 2.0 / (size)), 2)));
    }
    return resultVec;
}
int getStandardOffset(vector<int> v1, vector<int> v2) {
    if (v1.size() == v2.size()) {
        int offsetSum = 0;
        for (size_t i = 0; i < v1.size(); i++) {
            offsetSum += pow(v1[i] - v2[i], 2);
        }
        return offsetSum;
    } else {
        return -1;
    }
}
int main() {
    vector<vector<char>> faceData;
    vector<int> faceAnalysis;
    char faceID;
    int width, height;
    cin >> width >> height;
    for (size_t i = 0; i < height; i++) {
        vector<char> emptyVec;
        faceData.push_back(emptyVec);
        for (size_t j = 0; j < width; j++) {
            cin >> faceID;
            faceData[i].push_back(faceID);
        }
    }
    // cout << "Reading complete." << endl;
    for (size_t i = 0; i < faceData.size(); i++) {
        int count = 0;
        for (size_t j = 0; j < faceData[i].size(); j++) {
            if (faceData[i][j] == '1') {
                ++count;
            }
        }
        if (count != 0) {
            faceAnalysis.push_back(count);
        }
    }
    vector<int> v1 = generateCircle(
        faceAnalysis.size(),
        *std::max_element(std::begin(faceAnalysis), std::end(faceAnalysis)));
    vector<int> v2 = generateSquare(
        faceAnalysis.size(),
        *std::max_element(std::begin(faceAnalysis), std::end(faceAnalysis)));
    vector<int> v3 = generateTriangle(
        faceAnalysis.size(),
        *std::max_element(std::begin(faceAnalysis), std::end(faceAnalysis)));
    // cout << "-----------------------" << endl
    //      << *std::max_element(std::begin(faceAnalysis),
    //      std::end(faceAnalysis))
    //      << endl
    //      << "---------------------------" << endl;
    // for (auto i : faceAnalysis) {
    //     cout << i << ' ';
    // }
    // cout << endl;
    // for (auto i : v1) {
    //     cout << i << ' ';
    // }
    // cout << endl;
    // for (auto i : v2) {
    //     cout << i << ' ';
    // }
    // cout << endl;
    // for (auto i : v3) {
    //     cout << i << ' ';
    // }
    int offsetOne = getStandardOffset(faceAnalysis, v1);
    int offsetTwo = getStandardOffset(faceAnalysis, v2);
    int offsetThree = getStandardOffset(faceAnalysis, v3);
    // cout << offsetOne << endl
    //      << offsetTwo << endl
    //      << offsetThree << endl
    //      << "-----------------" << endl;
    if (offsetOne <= offsetTwo && offsetOne <= offsetThree) {
        cout << "circle";
    } else if (offsetTwo <= offsetOne && offsetTwo <= offsetThree) {
        cout << "square";
    } else if (offsetThree <= offsetOne && offsetThree <= offsetTwo) {
        cout << "triangle";
    } else {
        cout << "whatever.";
    }
}
