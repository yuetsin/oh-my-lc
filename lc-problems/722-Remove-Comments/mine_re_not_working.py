#!/usr/bin/env python

import re


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        return [line if line for line in re.sub(r'//.*?\n', '', re.sub(r'/\*.*?\*/', '', '\n'.join(source))).split('\n')]
