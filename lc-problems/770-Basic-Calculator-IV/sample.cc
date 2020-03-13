// written by @jasonsun0311

namespace string_util {
string join( const vector< string >& strs, string delimiter ) {
    if ( strs.size() == 0 )
        return "";
    string ret = strs[ 0 ];
    for ( int i = 1; i < strs.size(); ++i ) {
        ret = ret + delimiter + strs[ i ];
    }
    return ret;
}
}  // namespace string_util

class polynomial;

class tokenizer {
private:
    bool is_letter( char ch ) {
        return ( 'a' <= ch and ch <= 'z' ) or ( 'A' <= ch and ch <= 'Z' );
    }

    bool is_digit( char ch ) {
        return '0' <= ch and ch <= '9';
    }

public:
    string                str;
    int                   pos;
    int                   n;
    static constexpr char eof = '\n';

    tokenizer( const string& s ) : str( s.begin(), s.end() ), pos( 0 ), n( s.size() ) {}

    void trim_whitespace() {
        while ( str[ pos ] == ' ' )
            pos++;
    }

    string peek_two() {
        int    cnt = 0;
        string ret = "";
        for ( int i = pos; i < n; ++i ) {
            if ( str[ i ] != ' ' ) {
                ret += str[ i ];
                cnt++;
            }
            if ( cnt >= 2 )
                break;
        }
        return ret;
    }

    char peek() {
        for ( int i = pos; i < n; ++i ) {
            if ( str[ i ] != ' ' )
                return str[ i ];
        }
        return eof;
    }

    bool has_next() {
        return peek() != eof;
    }

    char next_char() {
        trim_whitespace();
        return str[ pos++ ];
    }

    string next_string() {
        trim_whitespace();
        string s = "";
        while ( pos < n and str[ pos ] != '*' and str[ pos ] != ' ' and is_letter( str[ pos ] ) ) {
            s += str[ pos++ ];
        }
        return s;
    }

    int next_number() {
        trim_whitespace();
        int sign = peek() == '-' ? -1 : 1;
        int acc  = 0;
        while ( peek() >= '0' and peek() <= '9' ) {
            acc = 10.0 * acc + ( next_char() - '0' );
        }
        return acc * sign;
    }

    polynomial next_polynomial();
};

class polynomial {
private:
    vector< string > extract_var( const string& term ) {
        tokenizer        in( term );
        vector< string > vars;
        while ( in.has_next() ) {
            if ( in.peek() == '*' ) {
                in.next_char();
            }
            else {
                vars.push_back( in.next_string() );
            }
        }
        sort( vars.begin(), vars.end() );
        return vars;
    }

public:
    unordered_map< string, int > terms;
    unordered_map< string, int > val_map;

    void insert_term( const string& s, int val ) {
        if ( terms.find( s ) == terms.end() )
            terms.emplace( s, val );
        else
            terms[ s ] += val;
    }

    polynomial() = default;

    polynomial( const vector< string >& val, const vector< int >& coef ) : terms() {
        if ( val.size() == 0 ) {
            terms[ "1" ] = std::accumulate( coef.begin(), coef.end(), 1, []( int x, int y ) { return x * y; } );
        }
        else {
            for ( int i = 0; i < val.size(); ++i ) {
                insert_term( val[ i ], coef[ i ] );
            }
        }
    }

    void set_substitution( const vector< string >& var, const vector< int >& val ) {
        for ( int i = 0; i < val.size(); ++i ) {
            val_map.emplace( var[ i ], val[ i ] );
        }
    }

    pair< string, int > substitute_and_reduce( const string& val, int coef ) {
        if ( val == "1" )
            return { val, coef };
        string    new_var  = "";
        int       new_coef = coef;
        tokenizer in( val );
        while ( in.has_next() ) {
            if ( in.peek() == '*' ) {
                in.next_char();
            }
            else {
                string str = in.next_string();
                if ( val_map.find( str ) == val_map.end() ) {
                    new_var += ( new_var == "" ? str : ( "*" + str ) );
                }
                else {
                    new_coef *= val_map[ str ];
                }
            }
        }
        if ( new_var.size() == 0 )
            new_var = "1";
        return { new_var, new_coef };
    }

    polynomial simplify() {
        unordered_map< string, int > new_poly;
        for ( const auto& [ var, coef ] : terms ) {
            auto [ new_var, new_coef ] = substitute_and_reduce( var, coef );
            if ( new_poly.find( new_var ) == new_poly.end() ) {
                new_poly.emplace( new_var, new_coef );
            }
            else {
                new_poly[ new_var ] += new_coef;
            }
            if ( new_poly[ new_var ] == 0 )
                new_poly.erase( new_var );
        }
        polynomial ret;
        ret.terms = new_poly;
        return ret;
    }

    polynomial& operator+=( const polynomial& p ) {
        for ( const auto& [ var, coeff ] : p.terms ) {
            if ( terms.find( var ) == terms.end() ) {
                terms.emplace( var, coeff );
            }
            else {
                terms[ var ] += coeff;
            }
        }
        return *this;
    }

    polynomial& operator-=( const polynomial& p ) {
        for ( const auto& [ var, coeff ] : p.terms ) {
            if ( terms.find( var ) == terms.end() ) {
                terms.emplace( var, -coeff );
            }
            else {
                terms[ var ] -= coeff;
            }
        }
        return *this;
    }

    string merge( const string& var1, const string& var2 ) {
        if ( var1 == "1" )
            return var2;
        else if ( var2 == "1" )
            return var1;
        else {
            vector< string > merged_var = extract_var( var1 + "*" + var2 );
            sort( merged_var.begin(), merged_var.end() );
            return string_util::join( merged_var, "*" );
        }
    }

    polynomial& operator*=( const polynomial& p ) {
        unordered_map< string, int > new_terms;
        for ( const auto& [ var1, coef1 ] : terms ) {
            for ( const auto& [ var2, coef2 ] : p.terms ) {
                string new_var  = merge( var1, var2 );
                int    new_coef = coef1 * coef2;
                if ( new_terms.find( new_var ) == terms.end() ) {
                    new_terms.emplace( new_var, new_coef );
                }
                else {
                    new_terms[ new_var ] += new_coef;
                }
            }
        }
        terms.clear();
        terms.insert( new_terms.begin(), new_terms.end() );
        return *this;
    }

    vector< string > to_string() {
        vector< pair< vector< string >, int > > s;
        for ( const auto& [ var, coef ] : terms ) {
            if ( var == "1" )
                s.push_back( { {}, coef } );
            else {
                s.push_back( { extract_var( var ), coef } );
            }
        }
        for ( int i = 0; i < s.size(); ++i ) {
            sort( s[ i ].first.begin(), s[ i ].first.end() );
        }

        auto comp1 = []( const pair< vector< string >, int >& x, const pair< vector< string >, int >& y ) {
            if ( x.first.size() == y.first.size() )
                return lexicographical_compare( x.first.begin(), x.first.end(), y.first.begin(), y.first.end() );
            else
                return x.first.size() > y.first.size();
        };

        auto organizer = []( pair< vector< string >, int > s ) {
            if ( s.first.size() == 0 )
                return std::to_string( s.second );
            return std::to_string( s.second ) + "*" + string_util::join( s.first, "*" );
        };

        sort( s.begin(), s.end(), comp1 );
        vector< string > final_output;
        std::transform( s.begin(), s.end(), std::back_inserter( final_output ), organizer );
        return final_output;
    }
};

std::ostream& operator<<( std::ostream& os, const polynomial& poly ) {
    for ( const auto& [ key, val ] : poly.terms ) {
        cout << key << " : " << val << ", ";
    }
    return os;
}

polynomial tokenizer::next_polynomial() {
    vector< int >    coef;
    vector< string > val;
    trim_whitespace();
    while ( pos < n and ( peek() == '*' || is_digit( peek() ) || is_letter( peek() ) ) ) {
        if ( peek() == '*' ) {
            if ( peek_two()[ 1 ] == '(' ) {
                break;
            }
            next_char();
        }
        else if ( is_digit( peek() ) ) {
            coef.push_back( next_number() );
        }
        else {
            val.push_back( next_string() );
        }
    }
    sort( val.begin(), val.end() );
    string final_val  = string_util::join( val, "*" );
    int    final_coef = std::accumulate( coef.begin(), coef.end(), 1, []( int x, int y ) { return x * y; } );
    if ( final_val.size() == 0 )
        final_val = "1";
    polynomial ret( { final_val }, { final_coef } );
    return ret;
}

class Solution {
    /*
      Expr   = Term (+/- Term)
      Term   = Factor (* Factor)
      Factor = (Expr) | Polynomial
    */
public:
    vector< string > basicCalculatorIV( string expression, vector< string >& evalvars, vector< int >& evalints ) {
        tokenizer in( expression );

        std::function< polynomial( void ) > expr;
        std::function< polynomial( void ) > term;
        std::function< polynomial( void ) > factor;

        expr = [&]() {
            polynomial acc = term();
            while ( in.has_next() and ( in.peek() == '+' or in.peek() == '-' ) ) {
                char op = in.next_char();
                if ( op == '+' )
                    acc += term();
                else
                    acc -= term();
            }
            return acc;
        };

        term = [&]() {
            polynomial acc = factor();
            while ( in.has_next() and in.peek() == '*' ) {
                in.next_char();
                acc *= factor();
            }
            return acc;
        };

        factor = [&]() {
            polynomial acc;
            if ( in.has_next() and in.peek() == '(' ) {
                in.next_char();
                acc = expr();
                in.next_char();
            }
            else {
                acc = in.next_polynomial();
            }
            return acc;
        };
        polynomial result = expr();
        result.set_substitution( evalvars, evalints );
        return result.simplify().to_string();
    }
};
