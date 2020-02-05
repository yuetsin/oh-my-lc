#!/usr/bin/env python


class Solution():
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        hashtable = {}
        indextable = {}

        if not list1 or not list2:
            return None

        for i in range(len(list1)):
            hashtable[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in hashtable:  # restaurant from list2 in hashtable keys
                if hashtable[list2[i]] + i not in indextable:  # sumindex not in indextable
                    # create key sumindex with value list(restaurant)
                    indextable[hashtable[list2[i]] + i] = [list2[i]]
                else:  # sumindex in indextable
                    # append restaurant to value list(restaurant) for key with same indexsum
                    indextable[hashtable[list2[i]] + i].append(list2[i])

        return indextable[min(indextable)]
