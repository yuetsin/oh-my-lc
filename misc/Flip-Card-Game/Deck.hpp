#include "Card.hpp"
#include <vector>
#include <iostream>
#include <algorithm>

class Deck {
private:
    int               width;
    int               height;
    std::vector<char> char_list;
    std::vector<Card> card_list;

    Card* find_card(int x, int y) {
        for (size_t i = 0; i < card_list.size(); i++) {
            if (this->card_list[i].judge(x, y)) {
                return &(this->card_list[i]);
            }
        }
        return nullptr;
    }

    void init_deck() {
        int card_count = width * height;

        for (size_t i = 0; i < width; i++) {
            for (size_t j = 0; j < height; j++) {
                card_list.push_back(Card(i, j, this->char_list[i * height + j]));
            }
        }
    }

public:
    Deck(int width, int height, std::vector<char> char_list) {
        if (width <= 0 || height <= 0) {
            std::cerr << "非法输入，拒绝生成 Deck" << std::endl;
            exit(-1);
        }
        if (width % 2 && height % 2) {
            /* 不能被 2 整除 */
            std::cerr << "输入是奇数张牌，拒绝生成 Deck" << std::endl;
            exit(-2);
        }
        if (width * height / 2 != char_list.size()) {
            std::cerr << "输入的牌 char 和棋盘大小不等，拒绝生成 Deck" << std::endl;
            exit(-3);
        }
        this->width  = width;
        this->height = height;
        this->char_list.reserve(char_list.size());
        this->char_list.insert(this->char_list.end(), char_list.begin(), char_list.end());
        this->char_list.insert(this->char_list.end(), char_list.begin(), char_list.end());
        std::random_shuffle(this->char_list.begin(), this->char_list.end());
        init_deck();
    }

    char find_card_char(int x, int y) {
        for (size_t i = 0; i < card_list.size(); i++) {
            if (this->card_list[i].judge(x, y)) {
                return this->card_list[i].card_char;
            }
        }
        return '\0';
    }

    std::string print_deck(int except_x = -1, int except_y = -1, int except_x_2 = -1, int except_y_2 = -1) {
        std::string result_str = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
        for (size_t x = 0; x < width; x++) {
            for (size_t y = 0; y < height; y++) {
                Card* result = find_card(x, y);
                if (result) {
                    if ((x == except_x && y == except_y) || (x == except_x_2 && y == except_y_2)) {
                        result_str += "\t";
                        result_str += result->card_char;
                    }
                    else {
                        result_str += "\t?";
                    }
                }
                else {
                    result_str += "\t ";
                }
            }
            result_str += "\n";
        }
        return result_str;
    }

    void remove_cards(int except_x = -1, int except_y = -1, int except_x_2 = -1, int except_y_2 = -1) {
        for (std::vector<Card>::iterator it = card_list.begin(); it != card_list.end();) {
            if (it->judge(except_x, except_y) || it->judge(except_x_2, except_y_2)) {
                it = card_list.erase(it);
            }
            else {
                ++it;
            }
        }
    }

    bool check_if_over() {
        return card_list.size() == 0;
    }
};