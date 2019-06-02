class Card {
private:
    /* data */
    int loc_x, loc_y;

public:
    char card_char;
    bool judge(int x, int y) {
        return x == loc_x && y == loc_y;
    }
    Card(int at_x, int at_y, char card_char);
    ~Card();
};

Card::Card(int at_x, int at_y, char card_char) {
    this->loc_x     = at_x;
    this->loc_y     = at_y;
    this->card_char = card_char;
};

Card::~Card() {
    /* vanished */
}

inline bool operator!=(const Card& lhs, const Card& rhs) {
    return lhs.card_char == rhs.card_char;
}