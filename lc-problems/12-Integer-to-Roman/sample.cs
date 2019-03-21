public class Solution {
    public string IntToRoman(int num) {
        
        var romanChars = new string[] {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        var romanVals = new int[] {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        
        var resultBuilder = new StringBuilder();
        
        for (var j = 0; j < romanChars.Length; j++){
            if (num - romanVals[j] >= 0){
                for (var i = 0; i < num / romanVals[j]; i++){
                    resultBuilder.Append(romanChars[j]); 
                }
                
                num = num % romanVals[j];
            }
        }
        
        return resultBuilder.ToString();
    }
}