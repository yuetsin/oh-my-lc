#!/usr/bin/env python

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_line = [[0, 0, False, 0] for _ in range(capacity)]
        self.time = 0

    def get(self, key: int) -> int:
        # print(self.cache_line)
        self.time += 1
        for i in self.cache_line:
            if i[2] and i[0] == key:
                i[3] = self.time
                return i[1]
        return -1

    def put(self, key: int, value: int) -> None:
        self.time += 1
        index_i = self.get(key)
        if index_i != -1:
            for l in self.cache_line:
                if l[2] and l[0] == key:
                    l[1] = value
                    l[3] = self.time
                    return
            
        # print(self.cache_line)
        for i in self.cache_line:
            if not i[2]:
                i[0] = key
                i[1] = value
                i[2] = True
                i[3] = self.time
                return
        
        min_idx = None
        min_val = 1000000
        
        for i in range(len(self.cache_line)):
            if self.cache_line[i][3] < min_val:
                min_val = self.cache_line[i][3]
                min_idx = i
            
        # print("evict key %d" % self.cache_line[min_idx][0])
        self.cache_line[min_idx][0] = key
        self.cache_line[min_idx][1] = value
        self.cache_line[min_idx][2] = True
        self.cache_line[min_idx][3] = self.time
            
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)