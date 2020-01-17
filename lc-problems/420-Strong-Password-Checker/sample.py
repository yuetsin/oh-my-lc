#!/usr/bin/env python


class Solution:

    #  takes in the string, outputs a list of runs of
    #  a single character of 3 or more
    #  ex: "aaaaabbbbbbccdeeee" -> [5,6,4]
    def lengthCheck(self, s: str) -> List[int]:
        l = []
        curr = 1
        for i in range(1, len(s)):
            if (s[i] is s[i-1]):
                curr += 1
            else:
                if (curr > 2):
                    l.append(curr)
                curr = 1
        if (curr > 2):
            l.append(curr)
        return l

    # return 1 if we are missing an uppercase
    def uppercaseCheck(self, s: str) -> int:
        if (re.search("[A-Z]", s) is None):
            return 1
        return 0

    # return 1 if we are missing a lowercase
    def lowercaseCheck(self, s: str) -> int:
        if (re.search("[a-z]", s) is None):
            return 1
        return 0

    # return 1 if we are missing a number
    def numberCheck(self, s: str) -> int:
        if (re.search("[0-9]", s) is None):
            return 1
        return 0

    def strongPasswordChecker(self, s: str) -> int:
        leng = len(s)

        # If the password is 4 or less, then there is always a way
        # to just add characters until it is length 6 and make a
        # strong password
        if (leng <= 4):
            return 6-leng

        lis = self.lengthCheck(s)

        # For length 5, we only need to add 2 characters
        # if we are missing two types
        if (leng is 5):
            if (self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s) == 2):
                return 2
            return 1

        # If the length is acceptable, then all the changes can be replacements.
        # We need to make replacements to eliminate runs
        # ex: aaaaaaaa -> aaxaaxaa
        # hence the quotient by 3 rounded down.
        # If that number is lower than the missing types
        # then take the missing types
        if (leng <= 20):
            return max(sum(map(lambda x: int(x/3), lis)), self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s))

        # for too long passwords...
        if (leng > 20):
            # we first count how many deletions we need
            numdel = leng-20

            # the amount of replacements due to runs we would need
            # is reduced by the deletions
            runreplace = sum(map(lambda x: int(x/3), lis))

            # order the runs by how many deletions needed
            # to eliminate one replacement
            # ex. aaa needs 1 deletion, aaaa needs 2, aaaaa needs 3
            l = list(map(lambda x: (x % 3)+1, lis))
            l.sort()

            # variable to keep track of how many deletions are left
            rem = numdel

            # first the cheap ones:
            # aaa -> aa is one deletion to save one replacement
            for i in range(0, len(l)):
                if (rem >= l[i]):
                    rem -= l[i]
                    runreplace -= 1

            # after the cheap ones, take the most expensive ones
            # ex aaaaa -> aa saves 1 replacement, aaaaaaaa -> aa saves 2 replacements.
            # This calculation might make runreplace negative
            runreplace -= int(rem / 3)

            # if we need more replacements due
            # to the checks (or runreplace is negative)
            # make the number of replacements correct
            if (runreplace < self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s)):
                runreplace = self.uppercaseCheck(
                    s) + self.lowercaseCheck(s) + self.numberCheck(s)

            # total changes
            return numdel + runreplace
        return 0
