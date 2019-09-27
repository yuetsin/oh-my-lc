#!/usr/bin/env ruby

def missing_number(nums)
    nums.zip(1.step).flatten.reduce(:^)
end