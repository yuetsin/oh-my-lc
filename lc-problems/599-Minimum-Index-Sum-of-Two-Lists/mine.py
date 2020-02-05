#!/usr/bin/env python


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        mapp = {}

        for l2 in range(len(list2)):
            mapp.update({
                list2[l2]: l2
            })

        rresult = {}
        for wi in range(len(list1)):
            word = list1[wi]
            if word in mapp:
                rresult.update({
                    word: wi + mapp[word]
                })

        min_index_sum = min([v for k, v in rresult.items()])

        result = []

        for k, v in rresult.items():
            if v == min_index_sum:
                result.append(k)

        return result
