#!/usr/bin/env python

class LFUCache:

    def __init__(self, capacity: int):
        self.ddys = {}
        self.capacity = capacity
        self.global_timer = 0

    def get(self, key: int) -> int:
        self.global_timer += 1
        print("called get = %d" % key)
        
        if self.capacity == 0:
            return -1
        
        if key in self.ddys:
            self.ddys[key][1] += 1
            self.ddys[key][2] = self.global_timer
            return self.ddys[key][0]
        
        print(self.ddys)
        return -1

    def put(self, key: int, value: int) -> None:
        self.global_timer += 1
        print("called put = %d" % key)
        
        if self.capacity == 0:
            return
        
        if key in self.ddys:
            self.ddys[key][0] = value
            print("simple replace")
            print(self.ddys)
            return

        if len(self.ddys) >= self.capacity:
            # evict someone
            min_key = None
            min_freq = (0, float('+inf'), 0)
            for k, v in self.ddys.items():
                if v[1] < min_freq[1] or (v[1] == min_freq[1] and v[2] > min_freq[2]):
                    min_freq = v
                    min_key = k
            
            del self.ddys[min_key]
        self.ddys.update({
            key: [value, 0, self.global_timer]
        })
        print(self.ddys)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)