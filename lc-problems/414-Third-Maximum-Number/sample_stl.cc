class Solution {
public:
    int thirdMax( std::vector< int >& nums ) {
        const auto dim = nums.size();

        std::sort( nums.begin(), nums.end() );

        if ( nums.size() < 3 )
            return nums[ dim - 1 ];

        const auto it = std::unique( nums.begin(), nums.end() );

        nums.resize( std::distance( nums.begin(), it ) );

        if ( nums.size() < 3 )
            return nums[ dim - 1 ];

        return nums[ nums.size() - 3 ];
    }
};