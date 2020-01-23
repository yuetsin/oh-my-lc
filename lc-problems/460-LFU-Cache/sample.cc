class LFUCache {
public:
    // key, val, freq.
    unordered_map <int,list<tuple<int,int,int>>::iterator> keyiters;
    unordered_map <int,list<tuple<int,int,int>>> freqbuckets;
    
    int capacity;
    int min_freq;
    
    LFUCache (int capacity) 
    {
        this->capacity = capacity;
        min_freq = INT_MAX;
    }
    
    int get (int key) 
    {
        // get value to return.
        if (keyiters.count (key) == 0)
            return -1;
        
        // return value.
        int val = std::get <1> (*keyiters [key]);
        
        // erase old freq.
        int freq = erase (key);
        
        // insert new freq.
        insert (key, val, ++freq);
        
        // done.
        return val;
    }
    
    void put(int key, int val) 
    {
        // sanity check.
        if (capacity == 0)
            return;
        
        // already present, erase and insert with new freq, value.
        if (keyiters.count (key))
        {
            int freq = erase (key);
            insert (key, val, ++freq);
            return;
        }
        
        // evict.
        if (keyiters.size () >= capacity)
            erase (std::get <0> (*freqbuckets [min_freq].begin ()));
            
        // insert.
        insert (key, val, 1);
    }
    
    int erase (int key)
    {
        // find bucket.
        int freq = std::get <2> (*keyiters [key]);
            
        // erase key from bucket.
        freqbuckets [freq].erase (keyiters [key]);
        
        // erase bucket.
        if (freqbuckets [freq].empty ())
        {
            freqbuckets.erase (freq);
            if (min_freq == freq)
                min_freq = INT_MAX;
        }
        
        // erase index.
        keyiters.erase (key);
        
        // done.
        return freq;
    }
    
    void insert (int key, int val, int freq)
    {
        // insert into bucket.
        freqbuckets [freq].emplace_back (key, val, freq);
        
        // index.
        keyiters [key] = prev (freqbuckets [freq].end ());
        
        // update min_freq.
        min_freq = min (min_freq, freq);
    }
};