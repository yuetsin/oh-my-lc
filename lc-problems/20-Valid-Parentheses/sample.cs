public class Solution {
    public bool IsValid(string s) {
        Stack<char> expr = new Stack<char>();
        foreach (var character in s)
        {
            if(expr.Count == 0 || character.Equals('(') || character.Equals('[') || character.Equals('{'))
            {
                expr.Push(character);
            }
            else
            {
                if(character.Equals('}'))
                {//found closing bracket compare with 
                    if(expr.Peek().Equals('{'))
                    {
                        expr.Pop();
                    }
                    else
                    {
                        expr.Push(character);
                    }
                }
                else if(character.Equals(')'))
                {
                    if(expr.Peek().Equals('('))
                    {
                        expr.Pop();
                    }
                    else
                    {
                        expr.Push(character);
                    }
                }
                else if(character.Equals(']'))
                {
                    if(expr.Peek().Equals('['))
                    {
                        expr.Pop();
                    }
                    else
                    {
                        expr.Push(character);
                    }
                }
            }
        }
        return expr.Count == 0;
    }
}