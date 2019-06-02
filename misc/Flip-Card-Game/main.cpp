#include "Deck.hpp"
#include <iostream>

#ifdef __WIN32__
#include <windows.h>
#define sleep(x) Sleep(( x )*1000)
#else
#include <unistd.h>
#endif

using namespace std;

bool check_valid(int x, int y, int width, int height) {
    if (x < 0 || x >= width) {
        return false;
    }
    if (y < 0 || y >= height) {
        return false;
    }
    return true;
}

int main() {
    int          width = 4, height = 4;
    vector<char> characters;
    characters.push_back('a');
    characters.push_back('p');
    characters.push_back('c');
    characters.push_back('t');
    characters.push_back('w');
    characters.push_back('n');
    characters.push_back('k');
    characters.push_back('x');
    Deck deck = Deck(width, height, characters);
    cout << deck.print_deck() << endl;
    int open_card_1_x = -1, open_card_1_y = -1, open_card_2_x = -1, open_card_2_y = -1;
    while (!deck.check_if_over()) {

        if (!check_valid(open_card_1_x, open_card_1_y, width, height)) {
            cout << "输入你想要翻开的第一张牌，例如：x: 2 y: 2（用空格分开）" << endl;
            cin >> open_card_1_x >> open_card_1_y;
            --open_card_1_x;
            --open_card_1_y;
            if (!check_valid(open_card_1_x, open_card_1_y, width, height)) {
                cerr << "无效输入。请仔细检查。" << endl;
                open_card_1_x = -1, open_card_1_y = -1, open_card_2_x = -1, open_card_2_y = -1;
                continue;
            }

            if (deck.find_card_char(open_card_1_x, open_card_1_y) == '\0') {
                open_card_1_x = -1, open_card_1_y = -1, open_card_2_x = -1, open_card_2_y = -1;
                cout << deck.print_deck() << endl;
                cerr << "这张牌已经被拿走了哦。" << endl;
                continue;
            }

            else {
                cout << "您翻开了位于 " << open_card_1_x << "，" << open_card_1_y << " 的牌……" << endl;
                cout << deck.print_deck(open_card_1_x, open_card_1_y) << endl;
            }
        }
        else {
            cout << "输入你想要翻开的第二张牌，例如：x: 2 y: 2（用空格分开）" << endl;
            cin >> open_card_2_x >> open_card_2_y;
            --open_card_2_x;
            --open_card_2_y;

            if (!check_valid(open_card_2_x, open_card_2_y, width, height)) {
                open_card_1_x = -1, open_card_1_y = -1, open_card_2_x = -1, open_card_2_y = -1;
                cout << deck.print_deck() << endl;
                cerr << "无效输入。请仔细检查。" << endl;
                continue;
            }

            if (open_card_1_x == open_card_2_x && open_card_1_y == open_card_2_y) {
                open_card_1_x = -1, open_card_1_y = -1, open_card_2_x = -1, open_card_2_y = -1;
                cout << deck.print_deck() << endl;
                cerr << "这张牌已经被翻开了哦。" << endl;
                continue;
            }

            if (deck.find_card_char(open_card_2_x, open_card_2_y) == '\0') {
                open_card_1_x = -1, open_card_1_y = -1, open_card_2_x = -1, open_card_2_y = -1;
                cout << deck.print_deck() << endl;
                cerr << "这张牌已经被拿走了哦。" << endl;
                continue;
            }

            else {
                cout << "您翻开了位于 " << open_card_2_x << "，" << open_card_2_y << " 的牌……" << endl;

                if (deck.find_card_char(open_card_1_x, open_card_1_y) == deck.find_card_char(open_card_2_x, open_card_2_y)) {
                    deck.remove_cards(open_card_1_x, open_card_1_y, open_card_2_x, open_card_2_y);
                    cout << deck.print_deck() << endl;
                    open_card_1_x = -1, open_card_1_y = -1, open_card_2_x = -1, open_card_2_y = -1;
                    cout << "您成功的配对了一组扑克牌！" << endl;
                }
                else {
                    cout << deck.print_deck(open_card_1_x, open_card_1_y, open_card_2_x, open_card_2_y) << endl;
                    cout << "一秒后消失~" << endl;
                    sleep(1);
                    open_card_1_x = -1, open_card_1_y = -1, open_card_2_x = -1, open_card_2_y = -1;
                    cout << deck.print_deck();
                }
            }
        }
    }
    cout << "Good! 全部扑克牌都已经被清除!" << endl;
}