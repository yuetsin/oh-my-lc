func lengthOfLongestSubstring(s string) int {
    maxLength, curLength, startIndex := 0, 0, 0
    magic := map[rune]int{}
    
    for index, value := range(s) {
        if lastIndex, ok := magic[value]; ok && lastIndex >= startIndex {
            startIndex = lastIndex + 1
            curLength = index - lastIndex
        } else {
            curLength += 1
        }
        
        if curLength > maxLength {
            maxLength = curLength
        }
        
        magic[value] = index
    }

    return maxLength
}