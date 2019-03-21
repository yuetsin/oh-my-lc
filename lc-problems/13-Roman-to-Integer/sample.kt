class Solution {
    fun romanToInt(s: String): Int {
        
        var returnValue: Int = 0
        
        for(i in s.indices) {
            
            if(i == s.length-1) {
                returnValue += getValueFromCharacter(s[i])
                return returnValue
            }
            
            if(getValueFromCharacter(s[i]) >= getValueFromCharacter(s[i+1])) {
                returnValue += getValueFromCharacter(s[i])
            } else {
                returnValue -= getValueFromCharacter(s[i])
            }
        }
        
        return returnValue
    }
    
    fun getValueFromCharacter(c: Char): Int {
        when(c) {
            'I' -> return 1
            'V' -> return 5
            'X' -> return 10
            'L' -> return 50
            'C' -> return 100
            'D' -> return 500
            'M' -> return 1000
            else -> return 0
        }
    }
}