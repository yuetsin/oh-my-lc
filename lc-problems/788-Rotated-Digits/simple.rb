#!/usr/bin/env ruby

# written by @rosssg

# @param {Integer} n
# @return {Integer}
def rotated_digits(n)
    count = 0
    bad = ['3','4','7']
    good = ['2','5','6','9']
    for i in 2..n
        str_arr=i.to_s.chars
        count += 1 if (str_arr & good !=[]) and (str_arr & bad==[])
    end
    count
end