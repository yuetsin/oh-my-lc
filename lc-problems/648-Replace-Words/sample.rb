#!/usr/bin/env ruby

def replace_words(dict, sentence)
    words = sentence.split(" ")
    
    result = words.map do |word|
        replacement = word
        dict.each do |root|
            if word.start_with?(root) && replacement.length > root.length
                replacement = root
            end
        end
        replacement
    end
    
    result.join(" ")
end