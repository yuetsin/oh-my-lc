#!/usr/bin/env python


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        set_type = set(words)
        for word in words:
            wordlen = len(word)
            lptr = 0
            rptr = 1
            done = False
            count = 0
            while rptr < wordlen:
                print("judge %s" % word[lptr: rptr])
                if word[lptr: rptr] in set_type:
                    print("found %s" % word[lptr: rptr])
                    lptr = rptr
                    done = True
                    count += 1
                else:
                    done = False

                rptr += 1

            if done and count > 1:
                print("%s is concatenated." % word)
