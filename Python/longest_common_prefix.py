from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    prefix = strs[0]
    for i in range(1, len(strs)):
        curr_str = strs[i]
        for j in range(0, len(curr_str) + 1):
            try:
                if prefix[j] != curr_str[j]:
                    prefix = prefix[0:j]
            except IndexError:
                prefix = prefix[0:j]
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["reflower","flow","flight"]))
print(longestCommonPrefix(["ab", "a"]))