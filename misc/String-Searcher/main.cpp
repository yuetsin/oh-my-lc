//
//  main.cpp
//  String_searcher
//

#include <iostream>
#include <string>
using std::cin;
using std::cout;
using std::endl;
using std::getline;
using std::string;
using std::to_string;
bool debugMode = false;
// enable debugMode will destroy the interaction
void log(string logInfo) {
    cout << logInfo << endl;
}

void summary(int times, string name, bool nonsense = true) {
    if (nonsense) {
        cout << endl
             << "Now, the summary time!" << endl
             << "There" << (times == 1 ? " is " : " are ")
             << (times ? to_string(times) : "no any") << ' ' << '"' << name << '"'
             << (times == 1 ? " " : "s ")
             << "in this word." << endl;
    } else {
        cout << endl
             << times << ' ' << '"' << name << '"';
    }
    return;
}

int main() {
    if (debugMode) {
        const int lengthLimit = 80;
        log("Length limit:" + to_string(lengthLimit));
        size_t prevIndex = 0, currIndex = 0, keyWordLength = 0;
        int occurTimes = 0;
        string rawString = "", keyWord = "";
        cout << "Please enter some words... (less than " << lengthLimit << " chars)" << endl;
        getline(cin, rawString);
        log("Successfully read in the rawString");
        if (rawString.length() >= lengthLimit) {
            cout << "Invalid length." << endl;
            return -1;
        }
        cout << "Now, enter the character you want to find:" << endl;
        cin >> keyWord;
        log("Successfully read in the key word");
        keyWordLength = keyWord.length();
        prevIndex -= keyWordLength;
        cout << rawString << endl;
        while (true) {
            log("Go into the circulate");
            currIndex = rawString.find(keyWord, prevIndex + keyWordLength);
            if (currIndex != string::npos) {
                cout << string(currIndex - prevIndex - keyWordLength, ' ') << string(keyWordLength, '^');
                prevIndex = currIndex;
                log("prevIndex:" + to_string((prevIndex)));
                log("currIndex:" + to_string((currIndex)));
                ++occurTimes;
            } else {
                log("CirculateEnd");
                break;
            }
        }
        cout << endl
             << string(rawString.length(), '-');
        log("Go in to the Summary");
        summary(occurTimes, keyWord);
    } else {
        const int lengthLimit = 80;
        size_t prevIndex = 0, currIndex = 0, keyWordLength = 0;
        int occurTimes = 0;
        string rawString = "", keyWord = "";

        // 拿到两个字符串
        cout << "Please enter some words... (less than " << lengthLimit << " chars)" << endl;
        getline(cin, rawString);
        if (rawString.length() >= lengthLimit) {
            cout << "Invalid length." << endl;
            return -1;
        }
        cout << "Now, enter the character you want to find:" << endl;
        cin >> keyWord;
        keyWordLength = keyWord.length();
        prevIndex -= keyWordLength;
        cout << rawString << endl;

        // 开始循环搜索数据
        while (true) {
            currIndex = rawString.find(keyWord, prevIndex + keyWordLength);
            if (currIndex != string::npos) {
                cout << string(currIndex - prevIndex - keyWordLength, ' ') << string(keyWordLength, '^');
                prevIndex = currIndex;
                ++occurTimes;
            } else {
                // Jump out definition
                break;
            }
        }

        /*
         不再必要的判断
         if (!occurTimes) {
         cout << string(rawString.length(), '-')
         << "No match." << endl;
         return 1;
         }
         // 直接整合到 summary 里面就好了吧
         // 没必要在外面加一坨不好看的代码
         */

        // 开始做总结
        cout << endl
             << string(rawString.length(), '-');
        summary(occurTimes, keyWord);
    }
}
