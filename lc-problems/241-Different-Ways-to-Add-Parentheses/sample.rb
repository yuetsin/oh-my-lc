#!/usr/bin/env ruby

def diff_ways_to_compute(input)
    tokens = parse_token(input)
    parse(tokens)
end

def parse(x)
    return [x[0].to_i] if x.length == 1
    
    result = []
    (0..x.length-2).each do |i|
        next if i % 2 == 0
        val1 = parse(x[0...i])
        val2 = parse(x[i+1..-1])
        sign = x[i]
        
        val1.each do |k|
            val2.each do |y|
                if sign == "+"
                    result << k + y
                elsif sign == "-"
                    result << k - y
                else
                    result << k * y
                end
            end
        end
    end
    return result
end

def parse_token(x)
    x.split(/([\+\-*])/)
end