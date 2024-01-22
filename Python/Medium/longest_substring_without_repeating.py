# Unfinished

def lengthOfLongestSubstring(s: str) -> int:
    chars = []
    unique_lens = []
    combos = []
    current_len = 0
    for char in s:
        if char in chars:
            print("new combo triggered")
            unique_lens.append(current_len)
            combos = combos + [chars]
            chars = []
            current_len = 0
        else:
            chars.append(char)
            print(char)
            print(chars)
            current_len += 1
            #print(current_len)
            #print(unique_lens)
            #print(chars)

    #print (combos)
    max_len = 0
    for combo in combos:
        #print(combo)
        if len(combo) > max_len:
            max_len = len(combo)

    return max_len

print(lengthOfLongestSubstring("pwwkew"))