class Solution {
public:
    int splitArray( vector< int >& nums, int m ) {

        long long int ans = 0;
        int           n   = nums.size();
        for ( int i = 0; i < n; i++ )
            ans += nums[ i ];

        long long int l = 0;
        long long int r = ans;

        while ( l <= r ) {
            long long int mid = ( l + r ) / 2;
            // cout << l << " " << r << " " << mid << endl;
            int           cuts     = 0;
            long long int sum      = 0;
            bool          possible = true;
            for ( int i = 0; i < n; i++ ) {
                if ( nums[ i ] > mid ) {
                    possible = false;
                    break;
                }
                if ( sum + nums[ i ] <= mid )
                    sum += nums[ i ];
                else {
                    sum = nums[ i ];
                    cuts++;
                }
            }

            if ( cuts + 1 <= m && possible ) {
                r   = mid - 1;
                ans = min( ans, mid );
            }
            else {
                l = mid + 1;
            }
        }
        // cout << ans << endl;
        return ans;
    }
};