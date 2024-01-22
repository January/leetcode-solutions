def removeVowels(s: str) -> str:
    for c in s:
        if c in ["a", "e", "i", "o", "u"]:
            s.replace(str(c), "")
    return s