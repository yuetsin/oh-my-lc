#!/usr/bin/env python

import random
import string


class Codec:
    def __init__(self):
        self.mapping = {}
        self.available = string.printable

    def encode(self, longUrl: str) -> str:
        ext = ''.join(random.sample(self.available, k=2))
        self.mapping[ext] = longUrl
        return "http://tinyurl.com/"+ext

    def decode(self, shortUrl: str) -> str:
        return self.mapping[shortUrl[-2:]]
