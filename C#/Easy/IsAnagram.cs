public class Solution
{
    public bool IsAnagram(string s, string t)
    {
        char[] sCharArr = s.ToCharArray();
        char[] tCharArr = t.ToCharArray();

        Array.Sort(sCharArr);
        Array.Sort(tCharArr);

        return Enumerable.SequenceEqual(sCharArr, tCharArr);
    }
}