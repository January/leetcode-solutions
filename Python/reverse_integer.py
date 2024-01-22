# Runtime: 16ms (99.98%)
# Memory: 17.48MB (17.52%)

def reverse(x: int) -> int:
    string = str(x)
    string = string[::-1]
    if "-" in string:
        string = "-" + string.replace("-", "")
    retn = int(string)
    if (retn > 2**31 - 1) or (retn < -2**31):
        return 0
    else:
        return(int(string))

print(reverse(1534236469))