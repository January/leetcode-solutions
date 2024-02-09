def lengthOfLongestSubstring(s: str) -> int:
    start = result = 0
    seen = {}
    for i, char in enumerate(s):
        if seen.get(char, -1) >= start:
            start = seen[char] + 1
        result = max(result, i - start + 1)
        seen[char] = i
    return result