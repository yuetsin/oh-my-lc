#!/usr/bin/env python

from collections import OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity= capacity
        self.lst= OrderedDict()

    def get(self, key: int) -> int:
        if key in self.lst:
            tmp, freq = self.lst[key]
            del self.lst[key]
            self.lst[key] = [tmp, freq+1] 
            return tmp
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        if key in self.lst:
            _, freq= self.lst[key]
            del self.lst[key]
            self.lst[key]= [value, freq+1]
            
        elif len(self.lst) == self.capacity:
            keyLF, valfreq= sorted(self.lst.items(), key = lambda x: x[1][1])[0]
            minfreq= valfreq[1]
			
			# To check whether there is a key in the ordereddict with the same frequency and least recently used. If found delete that key.
            found= False
            for k, v in self.lst.items():
                if v[1]== minfreq:
                    del self.lst[keyLF]
                    found= True
                    break
            if not found:
                del self.lst[keyLF]
            
            self.lst[key]= [value, 0]
        else:
            self.lst[key]= [value, 0]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)