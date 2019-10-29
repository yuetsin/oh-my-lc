#!/usr/bin/env python

temp = Math.min(temp, k +  # 1. pay less
                Math.max(dp[i][k - 1], dp[k + 1][j]))  # 2. but asked for more

"""
It's like the game theory:

you wanna pay less
but your opponent asks for more
"""
