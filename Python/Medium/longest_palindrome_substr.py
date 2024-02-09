def longestPalindrome(s: str) -> str:
    if s == s[::-1]:
        return s
    longest = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(longest):
                longest = s[i:j]
    return longest

print(longestPalindrome("rockbottom"))