//
//  main.cpp
//  CalendarApp
//

#include <iostream>
#include <string>
using namespace std;

bool isLeapYear( int year ) {
    if ( year % 400 == 0 ) {
        return true;
    }
    else if ( year % 100 == 0 ) {
        return false;
    }
    else if ( year % 4 == 0 ) {
        return true;
    }
    else {
        return false;
    }
}

void TianGanDiZhiGenerator( int year, int& TianGan, int& DiZhi ) {
    if ( year < 0 || year > 3000 ) {
        return;
    }
    TianGan = ( year - 3 ) % 10 - 1;
    DiZhi   = ( year - 3 ) % 12 - 1;
}
int main() {
    int         firstDayWeekDatum          = 0;
    int         monthDays                  = 0;
    int         leapYearMonthsList[ 12 ]   = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
    int         commonYearMonthsList[ 12 ] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
    std::string weekDayNames[ 7 ]          = { "一", "二", "三", "四", "五", "六", "日" };
    std::string monthNames[ 12 ]           = { "一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二" };
    std::string TianGanList[ 10 ]          = { "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸" };
    std::string DiZhiList[ 12 ]            = { "子鼠", "丑牛", "寅虎", "卯兔", "辰龙", "巳蛇", "午马", "未羊", "申猴", "酉鸡", "戌狗", "亥猪" };
    int         year = 2017, month = 9;
    int         TianGan, DiZhi;
    cout << "Now, please enter the year and the month:" << endl;
    cin >> year >> month;
    firstDayWeekDatum = ( 1 + month * 2 + 3 * ( month + 1 ) / 5 + year + year / 4 - year / 100 + year / 400 ) % 7;
    if ( year < 0 || year > 3000 ) {
        return -1;
    }
    TianGanDiZhiGenerator( year, TianGan, DiZhi );
    cout << year << " " << TianGanList[ TianGan ] << DiZhiList[ DiZhi ] << "年 " << month << "月" << endl;
    for ( string i : weekDayNames ) {
        cout << i << ' ';
    }
    cout << endl;
    if ( isLeapYear( year ) ) {
        monthDays = leapYearMonthsList[ month - 1 ];
    }
    else {
        monthDays = commonYearMonthsList[ month - 1 ];
    }
    int circulateIndex = firstDayWeekDatum;
    cout << string( firstDayWeekDatum * 3, ' ' );
    for ( int i = 1; i <= monthDays; ++i ) {
        if ( i < 10 ) {
            cout << ' ' << i << ' ';
        }
        else {
            cout << i << ' ';
        }
        if ( ++circulateIndex == 7 ) {
            circulateIndex = 0;
            cout << endl;
        }
    }
    cout << endl;
}
