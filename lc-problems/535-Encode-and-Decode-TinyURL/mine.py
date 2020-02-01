#!/usr/bin/env python


class Codec:

    maps = {}
    max_v = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        str_v = str(self.max_v)
        self.maps.update({
            str_v: longUrl
        })
        self.max_v += 1
        return str_v

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.maps[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
